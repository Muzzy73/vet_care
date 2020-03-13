import csv


# bench execute vet_care.scripts.filter_from_history.execute --args "['./data/new_history.csv', './data/filtered.csv']"
def execute(input, output):
    filters = ['10163', '10196', '10197', '10198', '10199', '10200', '10207', '10208', '10212', '10216', '10218', '10228', '10229', '10231', '10236', '10237', '10240', '10241', '10247', '10255', '10259', '10265', '10272', '10280', '10283', '10288', '10299', '10305', '10307', '10308', '10310', '10311', '10317', '10327', '10329', '10330', '10335', '10336', '10337', '10338', '10339', '10340', '10341', '10342', '10343', '10344', '10345','10349', '10350', '10351', '10352', '10353', '10354', '10355', '10356', '10357', '10358', '10361', '10362', '10364', '10365', '10366', '10367', '10369', '10370', '10371', '10372', '10373', '10374', '10375', '10376', '10377', '10378', '10379', '10380', '10382', '10383', '10384', '10385', '10386', '10387', '10388', '10389', '10390', '10392', '10393', '10394', '10395', '10396', '10397', '10398', '10399', '10401', '10402', '10404', '10405', '10406', '10407', '10408', '10409', '10410', '10411', '10412', '10413', '10416', '10417', '10418', '10419', '10420', '10421', '10422', '10423', '10427', '10428', '10429', '10430', '10431', '10432', '10433', '10434', '10435', '10436', '10437', '10439', '10440', '10441', '10442', '10444', '10445', '10446', '10448', '10449', '10450', '10451', '10452', '10453', '10454', '10455', '10456', '10457', '10458', '10459', '10460', '10462', '10463', '10464', '10465', '10467', '10468', '10469', '10475', '10476', '10477','10478', '10479', '10480', '10481', '10482', '10483', '10484', '10485', '10488', '10489', '10490', '10491', '10492', '10493', '10494', '10495', '10496', '10497', '10499', '10500', '10501', '10502', '10505', '10506', '10507', '10508', '10509', '10511', '10512', '10513', '10514', '10515', '10516', '10517', '10518', '10519', '10520', '10521', '10522', '10523', '10524', '10525', '10527', '10528', '10529', '10530', '10531', '10532', '10533', '10534', '10535', '10539', '10540', '10541', '10542', '10543', '10544', '10546', '10551', '10553', '10557', '10558', '10561', '10562', '10564', '10567', '10568', '10569', '10571', '10572', '10573', '10574', '10575', '10576', '10578', '10579', '10581', '10582', '10583', '10584', '10586', '10587', '10588', '10589', '10590', '10591', '10594', '10595', '10599', '10601', '10603', '10604', '10606', '10607', '10608', '10609', '10610', '10611', '10612', '1362', '1530', '1683', '4684', '4806', '4900', '4947', '5201', '5467', '6166', '6171', '6200', '6412', '6461', '6462', '6606', '6743', '6834', '6978', '7255', '7315', '8347', '8385', '8691', '9200', '938', '9432', '9449', '9594', '9762', '9993']
    filtered_items = []
    fieldnames = []
    with open(input, 'r') as inputfile:
        reader = csv.DictReader(inputfile)
        fieldnames = reader.fieldnames
        for row in reader:
            id = row.get('AnimalID')
            if id in filters:
                filtered_items.append(dict(row))

    with open(output, 'w') as outputfile:
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in filtered_items:
            writer.writerow(item)