from math import log, log10

import numpy as np
import os
import pydicom
import cv2
import matplotlib.pyplot as plt
import random
import sys
from datetime import date, datetime, timedelta

from numpy import uint16
from pydicom.uid import generate_uid
from pydicom.valuerep import DA, DSfloat
from pydicom.datadict import dictionary_VR

UAS_CHOICES = [36000,36100,36200,36300,36400,36500,36600,36700,36800,36900]




def main():
    for i in range(0, 1):
        ds = pydicom.dcmread(sys.argv[1])
        image = ds.pixel_array

        # add poisson noise
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.array(np.random.poisson(image * vals) / float(vals),dtype=uint16)
        ds.PixelData = noisy.tobytes()

        # print(ds)
        patient_name = ds['PatientName']
        study_date = ds['StudyDate']
        image_date = ds[0x0008,0x0023]

        exposureInUas = ds[0x0018,0x1153]
        relativeExposure = ds[0x0018, 0x1405]
        exposureIndex = ds[0x0018,0x1411]
        deviationIndex = ds[0x0018,0x1413]
        exposureIndexTarget = ds[0x0018,0x1412]
        eiOld = exposureIndex.value

        eiT = exposureIndexTarget.value

        sopUID = ds[0x0008,0x0018]
        sopUID.value = generate_uid(prefix='9999.')

        #modify PatientName
        patient_name.value = 'TEST_QC'

        startDate = date(2022,11,6) # march, 1st

        newDate = startDate + timedelta(days=i)
        newDate = DA(newDate)


        #modify Exposure in µAs
        uasNew = random.choice(UAS_CHOICES)
        exposureInUas.value = uasNew
        eiNew = eiOld * uasNew / 36000.
        diNew = 10 * log10(eiNew/eiT)

        exposureIndex.value = DSfloat(eiNew,auto_format=True)
        deviationIndex.value = DSfloat(diNew,auto_format=True)
        study_date.value = newDate
        image_date.value = newDate

        ds.save_as('outTEST'+str(i)+'.dcm')


if __name__ == "__main__":
    main()
