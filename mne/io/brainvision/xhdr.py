from xmlConfigParser import XmlConfigParser

cfgValues = {
    'ExportInformation': {
        'ExportHistoryPath': '',
    },
    'DataFile': {},
    'MarkerFile': {},
    'DataOrientation': {},
    'BinaryFormat': {
        'Format': ''
    },
    'Properties': {
        'DataType': '',
        'DatasetLength' : 0,
        'SamplingInterval': 0,
        'DatasetUnit': '',
        'SegmentationType': '',
        'SegmentationTimeBased': 'true',
        'RefMarkerPosition': 0,
        'SegmentSize': 0,
        'Rereferenced': 'true',
        'AveragedSegments': 0
    }
}

cfg = XmlConfigParser(cfgValues, '/home/papadop/tmp/Damien/CS0030_BG_EMP_Average PS 17sept21 ordre new.xhdr', '')
cfg.parseXmlConfig()
print(cfg.get('ExportHistoryPath','ExportInformation'))
print(cfg.get('DataFile'))
print(cfg.get('MarkerFile'))
print(cfg.get('DataOrientation'))
print(cfg.get('Format','BinaryFormat'))
print(cfg.get('DataType','Properties'))
print(cfg.get('DatasetLength','Properties'))
print(cfg.get('SamplingInterval','Properties'))
print(cfg.get('DatasetUnit','Properties'))
print(cfg.get('SegmentationType','Properties'))
print(cfg.get('SegmentationTimeBased','Properties'))
print(cfg.get('RefMarkerPosition','Properties'))
print(cfg.get('SegmentSize','Properties'))
print(cfg.get('Rereferenced','Properties'))
print(cfg.get('AveragedSegments','Properties'))

## HACK: you can write your custom conditions and mess with default values and their optionality\
#                                                            before you run parseXmlConfig()
## if /optionalConfigSection is present: set default value for /nextConfig/whatever
#if not cfg.getRoot().find("basicConfig") is None:
#    cfg.set("new_value", "whatever", "nextConfig")
## HACK: this makes /nextConfig/whatever optional
#
## NOTE: parseXmlConfig will raise XmlConfigParserException if any of required options are missing
#cfg.parseXmlConfig()
#
## returns value of "whatever" from "nextConfig" section
#someValue = cfg.get("whatever", "nextConfig")
#
## converts to bool value of "bool" from "nextConfig" section
#boolValue = cfg.getBool("bool", "nextConfig")
#
## returns value of "whatever" from default section specified in constructor
#someOtherValue = cfg.get("optionalOption")
