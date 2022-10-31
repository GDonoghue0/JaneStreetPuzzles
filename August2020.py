J = 'AMDISHBANTMUSBACMAAPLDOSPGRMNVDALKQCOMCDWBAXPNRGPNCMSIVBWABCDNSCHWECLXLNXRXELINCYUMSFTNTAPDVNOVMCOFBHSICERNVRSNPSWKSUDREXRAYAEEOGCHTROPXDDRILMNOWFCCITWDCNPVHALLEGISRGPSADBENEMNSTSCOSTTWODFLTMOSLGWWHRLNTRSGEXPEGDLRCXOMLMTPRGOOGLWMTDGXCAHONLSNKETNFITBRK.BIOCBREQIXUNHFCCLCOPEPNWLTWTRVLOWSTZTSNADISCAGILDVAREGNBLLYBDXCMGMMMCKHCATOXYLNCLHXCMINTCBOEWELLCMCSALGNLOKCMEXPDOWUNPFEBAYCHRWATURINTUNMHKLACPRTGTJXJPMRKFRCTVAONUEVRGDEDLTROLFRTDYAMZNEEFXAEPWRKMXIMSCIEXCPBCTSHWMBKNGJNJCINFOXAIVZIONDAQDUKSSULTAESSLBF.BBYDHRBLKOTISYYAMCRMDLZBRAMETROWYNNIDXXUHSYFANGUALXNOCFGJNPRUAALBXPKIMASBUXAFLIRMKCTASYKMIQVRTXAMTBKRJFTIFFIVRSKMBSXAPAYCTLABMDTEIXAMATVIACNCTXSEEQRVORCLVSJMARFMCHPEAKAMPCHDHIIPGPCARROSTXNFLXADPZBHBIIBMYLUVTRHIGSREMROKEYSORLYVFCSCOTYLENWSAPHMKTXTFXHSTELANETFCXUPSXHPQHOLXAOSHESPYPLDISCKAPTVJKHYAVYAJGPPLABTADSKAIGJBHTHASHLTCOGPKGAVGOPPGAIZADMABBVANSSFASTFTVAVBPAYXAWKCVSFDXDOVFLSFISVAZOHUMAMGNWRBCOOPFGCVXCSXDFS'

with open('sp500.txt') as file:
    sp500 = file.read().splitlines()
for company in sp500:
    if company not in J:
        print(company)