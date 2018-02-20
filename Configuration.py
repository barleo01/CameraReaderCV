import configparser
import os
from pathlib import Path
import CameraParam


def CfgToDico():
    """ Copy cfg parameter to dictionary 
    """
    conffile = configparser.RawConfigParser()
    conffile.read('config.cfg')

    Dico = {
        "Brightness" : conffile.getfloat('CameraParameters', 'brightness_param'),
        "Contrast" : conffile.getfloat('CameraParameters', 'contrast_param'),
        "Exposure" : conffile.getfloat('CameraParameters', 'exposure_param'),
        "Saturation" : conffile.getfloat('CameraParameters', 'saturation_param'),
        "Gain" : conffile.getfloat('CameraParameters', 'gain_param'),
        "FPS" : conffile.getfloat('CameraParameters', 'fps_param')
    }
    return Dico

def DicoToCfg(CamParam):
    
    config = configparser.ConfigParser()
    config.read('config.cfg')
    config.add_section('CameraParameters')

    config.set('CameraParameters','brightness_param', str(CamParam['Brightness']))
    config.set('CameraParameters','contrast_param', str(CamParam['Contrast']))
    config.set('CameraParameters','exposure_param', str(CamParam['Exposure']))
    config.set('CameraParameters','saturation_param', str(CamParam['Saturation']))
    config.set('CameraParameters','gain_param', str(CamParam['Gain']))
    config.set('CameraParameters','fps_param', str(CamParam['FPS']))
    
    with open('config.cfg','w') as confi:
        config.write(confi)
    print("config.cfg file created")
    
    #close('config.cfg')
    

def ReadConfig ():
    conffile = Path("config.cfg")
    if conffile.is_file():
        # file exists
        #print("config file present")
        CameraParameters = CfgToDico()

    else:
        # file doesn't exists
        Dico_Param = {
            "Brightness" : 50,
            "Contrast" : 50,
            "Exposure" : 50,
            "Saturation" : 50,
            "Gain" : 50,
            "FPS" : 20
        }
        DicoToCfg(Dico_Param)
        CameraParameters = CfgToDico()
        
    return CameraParameters

        
def SaveConfig (param):
    #print("SaveConfig")
    os.remove('config.cfg')
    DicoToCfg(param)

