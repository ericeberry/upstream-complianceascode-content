import string

HEADERS = [
    'IA Control', 'CCI', 'SRGID', 'STIGID', 'SRG Requirement', 'Requirement',
    'SRG VulDiscussion', 'Vul Discussion', 'Status', 'SRG Check', 'Check', 'SRG Fix',
    'Fix', 'Severity', 'Mitigation', 'Artifact Description', 'Status Justification'
    ]
COLUMNS = string.ascii_uppercase[:17]  # A-Q uppercase letters
COLUMN_MAPPINGS = dict(zip(COLUMNS, HEADERS))


def get_iacontrol_mapping(srg_id: str) -> dict:
    if srg_id.startswith("SRG-OS-"):
        return srgid_to_iacontrol_gpos
    elif srg_id.startswith("SRG-APP-"):
        return srgid_to_iacontrol_ctr
    else:
        return None


srgid_to_iacontrol_gpos = {
    'SRG-OS-000001-GPOS-00001': 'AC-2 (1)',
    'SRG-OS-000002-GPOS-00002': 'AC-2 (2)',
    'SRG-OS-000004-GPOS-00004': 'AC-2 (4)',
    'SRG-OS-000021-GPOS-00005': 'AC-7 a',
    'SRG-OS-000023-GPOS-00006': 'AC-8 a',
    'SRG-OS-000024-GPOS-00007': 'AC-8 b',
    'SRG-OS-000027-GPOS-00008': 'AC-10',
    'SRG-OS-000028-GPOS-00009': 'AC-11 b',
    'SRG-OS-000029-GPOS-00010': 'AC-11 a',
    'SRG-OS-000030-GPOS-00011': 'AC-11 a',
    'SRG-OS-000031-GPOS-00012': 'AC-11 (1)',
    'SRG-OS-000032-GPOS-00013': 'AC-17 (1)',
    'SRG-OS-000033-GPOS-00014': 'AC-17 (2)',
    'SRG-OS-000037-GPOS-00015': 'AU-3 a',
    'SRG-OS-000038-GPOS-00016': 'AU-3 b',
    'SRG-OS-000039-GPOS-00017': 'AU-3 c',
    'SRG-OS-000040-GPOS-00018': 'AU-3 d',
    'SRG-OS-000041-GPOS-00019': 'AU-3 e',
    'SRG-OS-000042-GPOS-00020': 'AU-3 (1)',
    'SRG-OS-000042-GPOS-00021': 'AU-3 (1)',
    'SRG-OS-000046-GPOS-00022': 'AU-5 a',
    'SRG-OS-000051-GPOS-00024': 'AU-6 (4)',
    'SRG-OS-000054-GPOS-00025': 'AU-7 (1)',
    'SRG-OS-000055-GPOS-00026': 'AU-8 a',
    'SRG-OS-000057-GPOS-00027': 'AU-9 a',
    'SRG-OS-000058-GPOS-00028': 'AU-9 a',
    'SRG-OS-000059-GPOS-00029': 'AU-9 a',
    'SRG-OS-000062-GPOS-00031': 'AU-12 a',
    'SRG-OS-000063-GPOS-00032': 'AU-12 b',
    'SRG-OS-000064-GPOS-00033': 'AU-12 c',
    'SRG-OS-000066-GPOS-00034': 'IA-5 (2) (b) (1)',
    'SRG-OS-000067-GPOS-00035': 'IA-5 (2) (a) (1)',
    'SRG-OS-000068-GPOS-00036': 'IA-5 (2) (a) (2)',
    'SRG-OS-000069-GPOS-00037': 'IA-5 (1) (h)',
    'SRG-OS-000070-GPOS-00038': 'IA-5 (1) (h)',
    'SRG-OS-000071-GPOS-00039': 'IA-5 (1) (h)',
    'SRG-OS-000072-GPOS-00040': 'IA-5 (1) (h)',
    'SRG-OS-000073-GPOS-00041': 'IA-5 (1) (d)',
    'SRG-OS-000074-GPOS-00042': 'IA-5 (1) (c)',
    'SRG-OS-000075-GPOS-00043': 'IA-5 (1) (h)',
    'SRG-OS-000076-GPOS-00044': 'IA-5 (1) (h)',
    'SRG-OS-000078-GPOS-00046': 'IA-5 (1) (h)',
    'SRG-OS-000079-GPOS-00047': 'IA-6',
    'SRG-OS-000080-GPOS-00048': 'AC-3',
    'SRG-OS-000095-GPOS-00049': 'CM-7 a',
    'SRG-OS-000096-GPOS-00050': 'CM-7 b',
    'SRG-OS-000104-GPOS-00051': 'IA-2',
    'SRG-OS-000105-GPOS-00052': 'IA-2 (1)',
    'SRG-OS-000106-GPOS-00053': 'IA-2 (2)',
    'SRG-OS-000107-GPOS-00054': 'IA-2 (1)',
    'SRG-OS-000108-GPOS-00055': 'IA-2 (2)',
    'SRG-OS-000109-GPOS-00056': 'IA-2 (5)',
    'SRG-OS-000112-GPOS-00057': 'IA-2 (8)',
    'SRG-OS-000113-GPOS-00058': 'IA-2 (8)',
    'SRG-OS-000114-GPOS-00059': 'IA-3',
    'SRG-OS-000118-GPOS-00060': 'AC-2 (3) (a)',
    'SRG-OS-000120-GPOS-00061': 'IA-7',
    'SRG-OS-000121-GPOS-00062': 'IA-8',
    'SRG-OS-000122-GPOS-00063': 'AU-7 a',
    'SRG-OS-000123-GPOS-00064': 'AC-2 (2)',
    'SRG-OS-000125-GPOS-00065': 'MA-4 c',
    'SRG-OS-000132-GPOS-00067': 'SC-2',
    'SRG-OS-000134-GPOS-00068': 'SC-3',
    'SRG-OS-000138-GPOS-00069': 'SC-4',
    'SRG-OS-000142-GPOS-00071': 'SC-5 (2)',
    'SRG-OS-000163-GPOS-00072': 'SC-10',
    'SRG-OS-000184-GPOS-00078': 'SC-24',
    'SRG-OS-000185-GPOS-00079': 'SC-28',
    'SRG-OS-000205-GPOS-00083': 'SI-11 a',
    'SRG-OS-000206-GPOS-00084': 'SI-11 b',
    'SRG-OS-000228-GPOS-00088': 'AC-8 c 1, AC-8 c 2, AC-8 c 2, AC-8 c 2, AC-8 c 3',
    'SRG-OS-000239-GPOS-00089': 'AC-2 (4)',
    'SRG-OS-000240-GPOS-00090': 'AC-2 (4)',
    'SRG-OS-000241-GPOS-00091': 'AC-2 (4)',
    'SRG-OS-000250-GPOS-00093': 'AC-17 (2)',
    'SRG-OS-000254-GPOS-00095': 'AU-14 (1)',
    'SRG-OS-000255-GPOS-00096': 'AU-3 f',
    'SRG-OS-000256-GPOS-00097': 'AU-9 a',
    'SRG-OS-000257-GPOS-00098': 'AU-9 a',
    'SRG-OS-000258-GPOS-00099': 'AU-9 a',
    'SRG-OS-000259-GPOS-00100': 'CM-5 (6)',
    'SRG-OS-000266-GPOS-00101': 'IA-5 (1) (h)',
    'SRG-OS-000269-GPOS-00103': 'SC-24',
    'SRG-OS-000274-GPOS-00104': 'AC-2 (1)',
    'SRG-OS-000275-GPOS-00105': 'AC-2 (1)',
    'SRG-OS-000276-GPOS-00106': 'AC-2 (1)',
    'SRG-OS-000277-GPOS-00107': 'AC-2 (1)',
    'SRG-OS-000278-GPOS-00108': 'AU-9 (3)',
    'SRG-OS-000279-GPOS-00109': 'AC-12',
    'SRG-OS-000280-GPOS-00110': 'AC-12 (1)',
    'SRG-OS-000281-GPOS-00111': 'AC-12 (2)',
    'SRG-OS-000297-GPOS-00115': 'AC-17 (1)',
    'SRG-OS-000298-GPOS-00116': 'AC-17 (9)',
    'SRG-OS-000299-GPOS-00117': 'AC-18 (1)',
    'SRG-OS-000300-GPOS-00118': 'AC-18 (1)',
    'SRG-OS-000303-GPOS-00120': 'AC-2 (4)',
    'SRG-OS-000304-GPOS-00121': 'AC-2 (1)',
    'SRG-OS-000312-GPOS-00122': 'AC-3 (4)',
    'SRG-OS-000312-GPOS-00123': 'AC-3 (4)',
    'SRG-OS-000312-GPOS-00124': 'AC-3 (4)',
    'SRG-OS-000324-GPOS-00125': 'AC-6 (10)',
    'SRG-OS-000326-GPOS-00126': 'AC-6 (8)',
    'SRG-OS-000327-GPOS-00127': 'AC-6 (9)',
    'SRG-OS-000329-GPOS-00128': 'AC-7 b',
    'SRG-OS-000337-GPOS-00129': 'AU-12 (3)',
    'SRG-OS-000341-GPOS-00132': 'AU-4',
    'SRG-OS-000342-GPOS-00133': 'AU-4 (1)',
    'SRG-OS-000343-GPOS-00134': 'AU-5 (1)',
    'SRG-OS-000344-GPOS-00135': 'AU-5 (2)',
    'SRG-OS-000348-GPOS-00136': 'AU-7 a',
    'SRG-OS-000349-GPOS-00137': 'AU-7 a',
    'SRG-OS-000350-GPOS-00138': 'AU-7 a',
    'SRG-OS-000351-GPOS-00139': 'AU-7 a',
    'SRG-OS-000352-GPOS-00140': 'AU-7 a',
    'SRG-OS-000353-GPOS-00141': 'AU-7 b',
    'SRG-OS-000354-GPOS-00142': 'AU-7 b',
    'SRG-OS-000355-GPOS-00143': 'SC-45 (1) (a)',
    'SRG-OS-000356-GPOS-00144': 'SC-45 (1) (b)',
    'SRG-OS-000358-GPOS-00145': 'AU-8 b',
    'SRG-OS-000359-GPOS-00146': 'AU-8 b',
    'SRG-OS-000360-GPOS-00147': 'CM-6 b, AU-9 (5)',
    'SRG-OS-000362-GPOS-00149': 'CM-11 (2)',
    'SRG-OS-000363-GPOS-00150': 'CM-3 (5)',
    'SRG-OS-000364-GPOS-00151': 'CM-5 (1) (a)',
    'SRG-OS-000365-GPOS-00152': 'CM-5 (1) (b)',
    'SRG-OS-000366-GPOS-00153': 'CM-14',
    'SRG-OS-000368-GPOS-00154': 'CM-7 (2)',
    'SRG-OS-000370-GPOS-00155': 'CM-7 (5) (b)',
    'SRG-OS-000373-GPOS-00156': 'IA-11',
    'SRG-OS-000373-GPOS-00157': 'IA-11',
    'SRG-OS-000373-GPOS-00158': 'IA-11',
    'SRG-OS-000375-GPOS-00160': 'IA-2 (6) (a)',
    'SRG-OS-000376-GPOS-00161': 'IA-2 (12)',
    'SRG-OS-000377-GPOS-00162': 'IA-2 (12)',
    'SRG-OS-000378-GPOS-00163': 'IA-3',
    'SRG-OS-000379-GPOS-00164': 'IA-3 (1)',
    'SRG-OS-000383-GPOS-00166': 'IA-5 (13)',
    'SRG-OS-000384-GPOS-00167': 'IA-5 (2) (b) (2)',
    'SRG-OS-000392-GPOS-00172': 'MA-4 (1) (a)',
    'SRG-OS-000393-GPOS-00173': 'MA-4 (6)',
    'SRG-OS-000394-GPOS-00174': 'MA-4 (6)',
    'SRG-OS-000395-GPOS-00175': 'MA-4 (7)',
    'SRG-OS-000396-GPOS-00176': 'SC-13 b',
    'SRG-OS-000403-GPOS-00182': 'SC-23 (5)',
    'SRG-OS-000404-GPOS-00183': 'SC-28 (1)',
    'SRG-OS-000405-GPOS-00184': 'SC-28 (1)',
    'SRG-OS-000420-GPOS-00186': 'SC-5 a',
    'SRG-OS-000423-GPOS-00187': 'SC-8',
    'SRG-OS-000424-GPOS-00188': 'SC-8 (1)',
    'SRG-OS-000425-GPOS-00189': 'SC-8 (2)',
    'SRG-OS-000426-GPOS-00190': 'SC-8 (2)',
    'SRG-OS-000432-GPOS-00191': 'SI-10 (3)',
    'SRG-OS-000433-GPOS-00192': 'SI-16',
    'SRG-OS-000433-GPOS-00193': 'SI-16',
    'SRG-OS-000437-GPOS-00194': 'SI-2 (6)',
    'SRG-OS-000439-GPOS-00195': 'SI-2 c',
    'SRG-OS-000445-GPOS-00199': 'SI-6 a',
    'SRG-OS-000446-GPOS-00200': 'SI-6 b',
    'SRG-OS-000447-GPOS-00201': 'SI-6 d',
    'SRG-OS-000458-GPOS-00203': 'AU-12 c',
    'SRG-OS-000461-GPOS-00205': 'AU-12 c',
    'SRG-OS-000462-GPOS-00206': 'AU-12 c',
    'SRG-OS-000463-GPOS-00207': 'AU-12 c',
    'SRG-OS-000465-GPOS-00209': 'AU-12 c',
    'SRG-OS-000466-GPOS-00210': 'AU-12 c',
    'SRG-OS-000467-GPOS-00211': 'AU-12 c',
    'SRG-OS-000468-GPOS-00212': 'AU-12 c',
    'SRG-OS-000470-GPOS-00214': 'AU-12 c',
    'SRG-OS-000471-GPOS-00215': 'AU-12 c',
    'SRG-OS-000471-GPOS-00216': 'AU-12 c',
    'SRG-OS-000472-GPOS-00217': 'AU-12 c',
    'SRG-OS-000473-GPOS-00218': 'AU-12 c',
    'SRG-OS-000474-GPOS-00219': 'AU-12 c',
    'SRG-OS-000475-GPOS-00220': 'AU-12 c',
    'SRG-OS-000476-GPOS-00221': 'AU-12 c',
    'SRG-OS-000477-GPOS-00222': 'AU-12 c',
    'SRG-OS-000478-GPOS-00223': 'SC-13 b',
    'SRG-OS-000479-GPOS-00224': 'AU-4 (1)',
    'SRG-OS-000480-GPOS-00225': 'CM-6 b',
    'SRG-OS-000480-GPOS-00226': 'CM-6 b',
    'SRG-OS-000480-GPOS-00227': 'CM-6 b',
    'SRG-OS-000480-GPOS-00228': 'CM-6 b',
    'SRG-OS-000480-GPOS-00229': 'CM-6 b',
    'SRG-OS-000480-GPOS-00230': 'CM-6 b',
    'SRG-OS-000480-GPOS-00232': 'CM-6 b',
    'SRG-OS-000481-GPOS-00481': 'SC-8',
    'SRG-OS-000590-GPOS-00110': 'AC-2 (3) (b)',
    'SRG-OS-000690-GPOS-00140': 'CM-7 (9) (b)',
    'SRG-OS-000705-GPOS-00150': 'IA-2 (6) (b)',
    'SRG-OS-000710-GPOS-00160': 'IA-5 (1) (b)',
    'SRG-OS-000720-GPOS-00170': 'IA-5 (1) (e)',
    'SRG-OS-000725-GPOS-00180': 'IA-5 (1) (f)',
    'SRG-OS-000730-GPOS-00190': 'IA-5 (1) (g)',
    'SRG-OS-000745-GPOS-00210': 'IA-8 (2) (a)',
    'SRG-OS-000755-GPOS-00220': 'MA-3 (5)',
    'SRG-OS-000775-GPOS-00230': 'SC-17 b',
    'SRG-OS-000780-GPOS-00240': 'SC-28 (3)',
    'SRG-OS-000785-GPOS-00250': 'SC-45',
}

srgid_to_iacontrol_ctr = {
 'SRG-APP-000014-CTR-000035': 'AC-17 (2)',
 'SRG-APP-000014-CTR-000040': 'AC-17 (2)',
 'SRG-APP-000023-CTR-000055': 'AC-2 (1)',
 'SRG-APP-000024-CTR-000060': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000025-CTR-000065': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000026-CTR-000070': 'AC-2 (4)',
 'SRG-APP-000027-CTR-000075': 'AC-2 (4)',
 'SRG-APP-000028-CTR-000080': 'AC-2 (4),AU-12 c',
 'SRG-APP-000029-CTR-000085': 'AC-2 (4)',
 'SRG-APP-000033-CTR-000090': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000033-CTR-000095': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000033-CTR-000100': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000038-CTR-000105': 'AC-4',
 'SRG-APP-000039-CTR-000110': 'AC-4',
 'SRG-APP-000065-CTR-000115': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000068-CTR-000120': 'AC-8 a',
 'SRG-APP-000069-CTR-000125': 'AC-8 b',
 'SRG-APP-000089-CTR-000150': 'AU-12 a,AU-12 b,AU-12 c,AU-3 (1),CM-6 b',
 'SRG-APP-000090-CTR-000155': 'AU-12 a,AU-12 b,AU-12 c,AU-3 (1),CM-6 b',
 'SRG-APP-000091-CTR-000160': 'AU-12 c',
 'SRG-APP-000092-CTR-000165': 'AU-14 (1),AU-4 (1),AU-6 (4)',
 'SRG-APP-000095-CTR-000170': 'AU-12 c,AU-3,MA-4 (1) (a)',
 'SRG-APP-000096-CTR-000175': 'AU-3',
 'SRG-APP-000097-CTR-000180': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000098-CTR-000185': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000099-CTR-000190': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000100-CTR-000195': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000100-CTR-000200': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000101-CTR-000205': 'AU-12 a,AU-12 b,AU-12 c,AU-3 (1),CM-6 b',
 'SRG-APP-000109-CTR-000215': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000111-CTR-000220': 'AU-14 (1),AU-4 (1),AU-6 (4)',
 'SRG-APP-000116-CTR-000235': 'AU-8 a',
 'SRG-APP-000118-CTR-000240': 'AU-9',
 'SRG-APP-000119-CTR-000245': 'AU-9',
 'SRG-APP-000120-CTR-000250': 'AU-9',
 'SRG-APP-000121-CTR-000255': 'AU-9',
 'SRG-APP-000122-CTR-000260': 'AU-9',
 'SRG-APP-000123-CTR-000265': 'AU-9',
 'SRG-APP-000126-CTR-000275': 'AU-9 (3),MA-4 (6),SC-13,SC-23',
 'SRG-APP-000131-CTR-000280': 'CM-5 (3)',
 'SRG-APP-000131-CTR-000285': 'CM-5 (3)',
 'SRG-APP-000133-CTR-000290': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000133-CTR-000295': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000133-CTR-000300': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000133-CTR-000305': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000133-CTR-000310': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000141-CTR-000315': 'CM-7 a,CM7,MA-4 c',
 'SRG-APP-000141-CTR-000320': 'CM-7 a',
 'SRG-APP-000142-CTR-000325': 'CM-7 b',
 'SRG-APP-000142-CTR-000330': 'AC-6 (8),CM-7 b,SC-4',
 'SRG-APP-000148-CTR-000335': 'IA-2,SC-10',
 'SRG-APP-000148-CTR-000340': 'IA-2',
 'SRG-APP-000148-CTR-000345': 'IA-2',
 'SRG-APP-000148-CTR-000350': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000149-CTR-000355': 'IA-2 (1),IA-2 (2)',
 'SRG-APP-000150-CTR-000360': 'IA-2 (1),IA-2 (2)',
 'SRG-APP-000151-CTR-000365': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000152-CTR-000370': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000153-CTR-000375': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000156-CTR-000380': 'IA-2 (8)',
 'SRG-APP-000157-CTR-000385': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000158-CTR-000390': 'IA-3',
 'SRG-APP-000163-CTR-000395': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000164-CTR-000400': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000165-CTR-000405': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000166-CTR-000410': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000167-CTR-000415': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000168-CTR-000420': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000169-CTR-000425': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000170-CTR-000430': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000171-CTR-000435': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000172-CTR-000440': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000173-CTR-000445': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000174-CTR-000450': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000177-CTR-000465': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000178-CTR-000470': 'IA-6',
 'SRG-APP-000181-CTR-000485': 'AU-7 a',
 'SRG-APP-000185-CTR-000490': 'CM7,MA-4 c',
 'SRG-APP-000190-CTR-000500': 'IA-11,IA-2,SC-10',
 'SRG-APP-000211-CTR-000530': 'SC-2',
 'SRG-APP-000219-CTR-000550': 'AU-9 (3),MA-4 (6),SC-13,SC-23',
 'SRG-APP-000225-CTR-000570': 'SC-24',
 'SRG-APP-000226-CTR-000575': 'SC-24',
 'SRG-APP-000233-CTR-000585': 'SC-3',
 'SRG-APP-000234-CTR-000590': 'AC-2 (2)',
 'SRG-APP-000243-CTR-000595': 'AC-6 (8),CM-7 b,SC-4',
 'SRG-APP-000243-CTR-000600': 'SC-4',
 'SRG-APP-000246-CTR-000605': 'SC-5,SC-5 (1),SI-16',
 'SRG-APP-000266-CTR-000625': 'SI-11 a',
 'SRG-APP-000290-CTR-000670': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000291-CTR-000675': 'AC-2 (4),AU-12 c',
 'SRG-APP-000292-CTR-000680': 'AC-2 (4),AU-12 c',
 'SRG-APP-000293-CTR-000685': 'AC-2 (4),AU-12 c',
 'SRG-APP-000294-CTR-000690': 'AC-2 (4),AU-12 c',
 'SRG-APP-000297-CTR-000705': 'AC-12 (1)',
 'SRG-APP-000317-CTR-000735': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000318-CTR-000740': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000319-CTR-000745': 'AC-2 (4),AU-12 c',
 'SRG-APP-000320-CTR-000750': 'AC-2 (4),AU-12 c',
 'SRG-APP-000340-CTR-000770': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000342-CTR-000775': 'AC-6 (8),CM-7 b,SC-4',
 'SRG-APP-000343-CTR-000780': 'AC-6 (9),CM-5 (1)',
 'SRG-APP-000345-CTR-000785': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000357-CTR-000800': 'AU-3,AU-4,AU-5 b,AU-9 (3)',
 'SRG-APP-000358-CTR-000805': 'AU-14 (1),AU-4 (1),AU-6 (4)',
 'SRG-APP-000359-CTR-000810': 'AU-5 (1)',
 'SRG-APP-000360-CTR-000815': 'AU-5 (2),SI-6 d',
 'SRG-APP-000374-CTR-000865': 'AU-8 b',
 'SRG-APP-000375-CTR-000870': 'AU-8 b',
 'SRG-APP-000378-CTR-000880': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000378-CTR-000885': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000378-CTR-000890': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000380-CTR-000900': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000381-CTR-000905': 'AC-6 (9),CM-5 (1)',
 'SRG-APP-000383-CTR-000910': 'CM-7 (1) (b)',
 'SRG-APP-000384-CTR-000915': 'CM-7 (2)',
 'SRG-APP-000386-CTR-000920': 'AC-3,AC-6 (10),CM-11 (2),CM-5 (1),CM-5 (6),CM-7 '
                              '(5) (b),IA-2,IA-2 (5)',
 'SRG-APP-000389-CTR-000925': 'IA-11,SC-10',
 'SRG-APP-000390-CTR-000930': 'IA-11',
 'SRG-APP-000391-CTR-000935': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000397-CTR-000955': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000400-CTR-000960': 'IA-5 (13)',
 'SRG-APP-000401-CTR-000965': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000402-CTR-000970': 'AC-2 (10),AC-2 (11),AC-2 (2),AC-2 (3),AC-7 '
                              'a,AC-7 b,IA-2 (12),IA-2 (3),IA-2 (4),IA-2 '
                              '(9),IA-4 e,IA-5 (1) (a),IA-5 (1) (b),IA-5 (1) '
                              '(c),IA-5 (1) (d),IA-5 (1) (e),IA-5 (1) (f),IA-5 '
                              '(2) (c),IA-5 (2) (d),IA-8 (1)',
 'SRG-APP-000409-CTR-000990': 'AU-12 c,AU-3,MA-4 (1) (a)',
 'SRG-APP-000411-CTR-000995': 'AU-9 (3),MA-4 (6),SC-13,SC-23',
 'SRG-APP-000412-CTR-001000': 'AU-9 (3),MA-4 (6),SC-13,SC-23',
 'SRG-APP-000414-CTR-001010': 'RA-5 (5)',
 'SRG-APP-000416-CTR-001015': 'AU-9 (3),MA-4 (6),SC-13,SC-23',
 'SRG-APP-000429-CTR-001060': 'SC-28 (1)',
 'SRG-APP-000431-CTR-001065': 'SC-39',
 'SRG-APP-000435-CTR-001070': 'SC-5,SC-5 (1),SI-16',
 'SRG-APP-000439-CTR-001080': 'SC-8',
 'SRG-APP-000441-CTR-001090': 'SC-8 (2)',
 'SRG-APP-000442-CTR-001095': 'SC-8 (2)',
 'SRG-APP-000447-CTR-001100': 'SI-10 (3)',
 'SRG-APP-000450-CTR-001105': 'SC-5,SC-5 (1),SI-16',
 'SRG-APP-000454-CTR-001110': 'SI-2 (6)',
 'SRG-APP-000454-CTR-001115': 'SI-2 (6)',
 'SRG-APP-000456-CTR-001125': 'SI-2 c',
 'SRG-APP-000456-CTR-001130': 'SI-2 c',
 'SRG-APP-000472-CTR-001170': 'SI-6 a',
 'SRG-APP-000473-CTR-001175': 'SI-6 b',
 'SRG-APP-000474-CTR-001180': 'AU-5 (2),SI-6 d',
 'SRG-APP-000492-CTR-001220': 'AU-12 c',
 'SRG-APP-000493-CTR-001225': 'AU-12 c',
 'SRG-APP-000494-CTR-001230': 'AU-12 c',
 'SRG-APP-000495-CTR-001235': 'AU-12 c',
 'SRG-APP-000496-CTR-001240': 'AU-12 c',
 'SRG-APP-000497-CTR-001245': 'AU-12 c',
 'SRG-APP-000498-CTR-001250': 'AU-12 c',
 'SRG-APP-000499-CTR-001255': 'AU-12 c',
 'SRG-APP-000500-CTR-001260': 'AU-12 c',
 'SRG-APP-000501-CTR-001265': 'AU-12 c',
 'SRG-APP-000502-CTR-001270': 'AU-12 c',
 'SRG-APP-000503-CTR-001275': 'AU-12 c',
 'SRG-APP-000504-CTR-001280': 'AU-12 c',
 'SRG-APP-000505-CTR-001285': 'AU-12 c',
 'SRG-APP-000506-CTR-001290': 'AU-12 c',
 'SRG-APP-000507-CTR-001295': 'AU-12 c',
 'SRG-APP-000508-CTR-001300': 'AU-12 c,AU-3,MA-4 (1) (a)',
 'SRG-APP-000509-CTR-001305': 'AC-2 (4),AU-12 c',
 'SRG-APP-000510-CTR-001310': 'AU-12 a,AU-12 b,AU-12 c,AU-3,AU-3 (1),CM-6 '
                              'b,MA-4 (1) (a)',
 'SRG-APP-000514-CTR-001315': 'AU-9 (3),MA-4 (6),SC-13,SC-23',
 'SRG-APP-000516-CTR-000790': 'AU-12 a,AU-12 b,AU-12 c,AU-3 (1),CM-6 b',
 'SRG-APP-000516-CTR-001325': 'CM-6 b',
 'SRG-APP-000516-CTR-001330': 'CM-6 b',
 'SRG-APP-000516-CTR-001335': 'CM-6 b',
 'SRG-APP-000560-CTR-001340': 'AC-17 (2)',
 'SRG-APP-000605-CTR-001380': 'IA-5 (2) (a)',
 'SRG-APP-000610-CTR-001385': 'IA-7',
 'SRG-APP-000635-CTR-001405': 'AU-9 (3),MA-4 (6),SC-13,SC-23',
 'SRG-APP-000645-CTR-001410': 'CM-7 b',
 }
