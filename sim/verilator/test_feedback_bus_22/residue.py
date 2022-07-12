import sys
sys.path.insert(0,"../../../../python-osi")
sys.path.insert(0,"../../../scripts")
from sigmath import *
from subcarrier_math import *

from numpy.fft import ifft, fft, fftshift


def _signed_value(value, bit_count):
    if value > 2**(bit_count - 1) - 1:
        value -= 2**bit_count 

    return value



def _load_hex_file(filepath):
    with open(filepath) as bootprogram:
        lines = bootprogram.readlines()

    words = [int(l,16) for l in lines]

    rf = []
    for w in words:
        real = _signed_value(w&0xffff, 16)
        imag = _signed_value((w >> 16) & 0xffff, 16)
        rf.append(np.complex(real,imag))
        # print "r", real, " i ", imag
        # print rf[0]
        # sys.exit(0)
    return rf



y = [

1.69889,
-0.279466,
0.346041,
-0.109513,
0.0826241,
-0.0352722,
0.0257348,
-0.00772952,
0.00323024,
-0.00308969,
0.004191,
-0.0042808,
0.00172851,
-0.010198,
-0.0124423,
-0.00176999,
-0.00924358,
-0.0168806,
-0.0166639,
-0.00662927,
-0.00435999,
-0.00544269,
-0.0151052,
-0.0094168,
-0.0142793,
-0.00164881,
-0.0102262,
-0.00945757,
-0.00705626,
-0.013614,
-0.012956,
-0.00531599,
0.000345345,
-0.00660444,
0.000458664,
-0.00204823,
0.000412934,
0.00627833,
0.00744154,
0.000720152,
0.0018799,
-0.000870059,
0.00320621,
0.00865691,
0.00450407,
0.0115209,
0.00774322,
0.0107052,
0.00388534,
0.0037352,
0.00563798,
0.00453256,
-0.00222565,
-0.00390465,
0.0063599,
0.00646338,
0.00397021,
0.00142127,
-0.00513232,
-0.00489867,
0.0023773,
-0.00562627,
0.00551479,
0.00932594,
0.0054752,
0.00928765,
0.00932619,
0.00454756,
0.0151796,
0.0181779,
0.0116507,
0.027207,
0.00757987,
0.0145898,
0.0157062,
0.0254579,
0.0143654,
0.0134012,
0.0272739,
0.0299966,
0.0217471,
0.0212694,
0.0176067,
0.019351,
0.0185991,
0.0264374,
0.0145672,
0.022325,
0.0176838,
0.0230365,
0.0257964,
0.0208636,
0.0208185,
0.0232811,
0.0162085,
0.0121411,
-0.0362089,
0.0178157,
0.0193947,
0.0179771,
0.0196439,
0.0197639,
0.00819409,
0.0164581,
0.00807251,
0.0103427,
0.0109518,
0.00644916,
0.00439189,
0.00603401,
0.00764229,
0.0137126,
0.00473417,
0.0169868,
0.0160624,
0.00394104,
0.00647126,
0.0114055,
0.0187353,
0.0190164,
0.0135986,
0.0120149,
0.0016595,
0.00908677,
0.00609391,
1.54254e-05,
0.00344664,
0.0179501,
-0.000541453,
0.00768701,
0.0110129,
0.00144752,
0.018932,
0.0176111,
0.0166938,
0.0206803,
0.0146826,
-0.000894175,
0.000793674,
0.0110891,
0.00945546,
0.0121604,
0.0299567,
0.0168291,
0.0155039,
0.0120979,
0.00779131,
-0.000310138,
0.00219942,
0.00578805,
0.0114474,
0.015428,
0.0186365,
0.00701623,
0.0123836,
0.00452591,
0.0348237,
0.00882846,
0.012906,
0.0127913,
0.0158793,
0.0131253,
0.0118242,
0.00252119,
0.0119356,
0.0108973,
0.0039104,
0.00550463,
0.0045596,
-0.00547293,
-0.00344426,
0.00363702,
0.00574452,
0.00384105,
0.0101388,
0.000823632,
0.0146511,
0.0110975,
0.0243528,
0.00394966,
0.00520224,
-0.00301369,
0.0139785,
0.00635405,
0.00799275,
-0.000126006,
0.00212298,
-0.010623,
-0.00225969,
-0.00909505,
-0.00901423,
0.0063343,
0.00887857,
0.00252614,
0.000550057,
0.000639115,
0.00744927,
-0.000921985,
0.00397348,
0.00568529,
-0.00493557,
0.00260614,
0.00244067,
0.00286517,
0.00592925,
-0.000240509,
-0.00778948,
-0.00526684,
-0.00213729,
-0.0158497,
-0.00361726,
0.00020144,
0.0162232,
-0.00161725,
-0.00228714,
0.00356503,
0.00177683,
-0.0120939,
0.00318995,
-0.0114031,
-0.0164438,
0.00766356,
-0.0135039,
0.00672108,
-0.00506901,
0.00999334,
-0.00141316,
0.00766948,
-2.74291e-05,
0.0118947,
0.00915264,
0.0059399,
0.00829974,
0.0166426,
0.00724788,
0.0174089,
0.0206191,
0.0155436,
0.0030331,
0.0145233,
0.0174112,
0.0115553,
0.00932834,
0.0178992,
0.00627147,
0.00599163,
0.0085571,
0.00621698,
0.00486109,
0.0187982,
0.00565827,
0.0130557,
0.00812744,
0.00960886,
0.0128615,
0.0140351,
0.015314,
0.00806856,
0.0051788,
0.0187217,
0.00657048,
0.0202757,
0.00260785,
0.0112897,
0.00436975,
0.0144998,
0.0142506,
0.00742806,
0.0146766,
0.00677913,
0.0112836,
0.0129146,
0.0159655,
0.00760553,
-0.00179355,
0.00247044,
0.00656017,
0.00524071,
0.00965717,
0.00561224,
0.00832366,
0.0120028,
0.00672996,
0.0115311,
0.0302364,
0.00855163,
0.00273693,
0.000868389,
-0.00582246,
0.0242269,
0.0156782,
0.0156942,
0.0116773,
0.00653944,
0.0146105,
0.0178805,
-0.000649425,
0.011895,
0.00446049,
0.00986583,
1.89717e-05,
0.00223815,
0.00534441,
0.00955663,
0.00936912,
0.0295461,
0.0212626,
0.0135668,
0.00076417,
-0.000347119,
-0.00704125,
-0.00589299,
-0.00703979,
-0.00105386,
-0.00449427,
-0.000579605,
0.00491492,
-1.73009e-05,
-0.00251681,
0.0117489,
0.0139373,
0.0275701,
0.0159764,
0.0161432,
0.0120984,
0.00243945,
0.0092888,
0.0187151,
0.0116214,
0.0113261,
0.0101124,
0.01501,
0.023167,
0.00264187,
0.00538818,
0.0234743,
0.0244026,
0.0193218,
0.0118381,
0.0158189,
0.0278604,
0.022421,
0.0133581,
0.0268888,
0.0283218,
0.02785,
0.0114802,
0.0286434,
0.0159938,
0.0130392,
0.0177372,
0.0171582,
0.0115985,
0.016822,
0.00230605,
0.0107429,
-0.000830158,
-0.00368823,
-0.000172169,
-0.00580611,
9.479e-05,
0.00803592,
0.00288063,
0.00903031,
0.0079623,
0.00610413,
0.00995978,
0.0237148,
0.0122146,
0.0172814,
0.00229378,
0.0131782,
0.00666664,
0.00627784,
0.00505984,
0.00646516,
0.00498958,
0.0147607,
-0.00487116,
0.022057,
0.00623162,
0.00760259,
0.00338458,
-0.00907925,
-0.011952,
0.00729598,
0.00109309,
-0.00615155,
-0.00234691,
0.00142927,
-0.00345731,
0.00158302,
-0.00353147,
0.00966105,
0.00800874,
0.00720596,
-0.00701405,
-0.00351478,
-0.00491247,
0.00103593,
-0.00473175,
0.00659532,
0.00791049,
0.00616097,
0.0114533,
0.00191164,
0.0058495,
-0.00314574,
-0.00261557,
-0.0014192,
-0.00899748,
0.00109047,
-0.00471671,
0.00283821,
0.000783133,
0.00485104,
0.00347186,
0.0129075,
0.00177054,
0.0119083,
0.0122514,
0.00583034,
0.000885154,
-0.00990029,
-0.00844117,
-0.000980019,
-0.00726861,
-0.0118775,
-0.000231638,
-0.00687798,
-0.00214527,
0.00293451,
0.0112223,
0.0140436,
-0.00283886,
0.012658,
0.00384239,
0.00475538,
0.0127143,
0.00621852,
0.0146961,
0.0251009,
0.0123597,
0.0121647,
0.0280594,
0.00112165,
0.00534584,
-0.00238078,
0.000469592,
-0.00174688,
-0.00409848,
-0.0011238,
-0.00526431,
-0.00600207,
-0.00989465,
-0.00362746,
0.00479385,
-0.000276579,
0.00457918,
-0.00139501,
0.00514054,
0.00125227,
-0.00171712,
0.00122262,
0.00714271,
0.00192891,
-0.00263608,
0.00588606,
0.00884431,
-0.00389655,
0.00159397,
0.00174096,
-0.00649414,
-0.00826717,
0.00143206,
-0.00788522,
-0.00817996,
-0.00889834,
-0.000571949,
-0.00476008,
-0.00137284,
-0.00755513,
-0.00843548,
-0.0249783,
0.00934737,
-0.00173262,
0.0100845,
0.00700466,
-0.000875076,
-0.00114807,
0.00155321,
0.00431286,
0.00144378,
0.00615723,
0.00956927,
0.00368081,
0.00261764,
-0.00414923,
0.00642452,
0.00143229,
0.0014646,
0.000177701,
0.010448,
0.00645561,
0.0117575,
0.00498244,
-0.00252012,
-0.00514399,
0.00635222,
0.0130964,
-0.00812956,
-0.00804801,
-0.00107035,
-0.0156957,
-0.00198454,
-0.00856525,
-0.00633957,
0.00156994,
-0.00460649,
0.00154315,
-0.00621759,
0.00424581,
-0.00295324,
-0.0128298,
-0.00516075,
-0.00232521,
0.00182369,
-0.00383188,
-0.0155271,
-0.00600133,
-0.00227151,
-0.0185197,
-0.00466592,
0.00681604,
0.000327344,
-0.012271,
-0.0051433,
-0.00406304,
-0.0108268,
-0.00204745,
-0.0135621,
-0.0194675,
-0.00771911,
-0.0180165,
-0.0151524,
-0.0119194,
-0.0171667,
-0.0211989,
-0.0220584,
-0.0125746,
-0.0102782,
-0.0149435,
-0.0152386,
-0.023244,
-0.0231898,
-0.00681058,
-0.0055002,
-0.0124159,
-0.0148444,
-0.0227338,
-0.024579,
-0.0226729,
-0.011508,
-0.0124141,
0.00224662,
-0.00557539,
-0.0190788,
-0.0123934,
-0.0128418,
-0.01145,
-0.000264071,
0.00615586,
0.00121517,
-0.00570336,
-0.00853299,
0.00311418,
-0.000825071,
0.00592017,
0.0226628,
0.0093383,
0.00340865,
0.00107336,
0.00175126,
-0.00441893,
-0.00234997,
-0.00486347,
-0.0096059,
-0.0127336,
-0.00912274,
-0.0127412,
-0.0179354,
-0.00778002,
-0.0249336,
-0.0176794,
-0.0170825,
-0.0156524,
-0.0235849,
-0.0218912,
-0.0280924,
-0.0205276,
-0.00989093,
-0.00878809,
-0.00948775,
-0.0118002,
-0.00139064,
-0.0129444,
-0.00730204,
-0.0100913,
-0.0119768,
-0.00694562,
5.39677,
0.588333,
0.517729,
-0.37503,
0.144835,
-0.112301,
0.00128918,
-6.9624,
0.728645,
-0.291355,
5.06605,
1.59164,
-0.55556,
0.355441,
-0.195032,
0.0897697,
-0.0856502,
0.0102471,
-0.0480753,
-0.0203602,
3.07093,
3.17781,
-3.41386,
-0.413846,
0.64136,
-5.03741,
-16.7566,
-10.2528,
0.0137317,
0.452229,
-0.337017,
-6.84298,
1.59894,
-1.09922,
0.539978,
4.69898,
1.62918,
-0.668512,
0.451212,
-0.25089,
0.131524,
-0.0971223,
0.0172101,
-0.0568692,
-0.0204104,
-0.0115327,
7.46652,
-1.5207,
0.533059,
-0.453761,
0.160539,
7.26314,
-7.47898,
1.30915,
-0.526038,
0.386749,
-6.54251,
0.125525,
-0.0935327,
0.0135121,
3.95833,
-2.98566,
3.483,
6.17077,
-0.52205,
0.0416748,
-0.12459,
0.0152746,
-0.0402521,
-0.0495495,
9.30292,
1.12298,
-4.41819,
-0.126877,
0.339573,
-0.104316,
10.8506,
1.09796,
0.403471,
0.125164,
0.0600687,
0.0252703,
-0.0936196,
-0.000273755,
-0.0458866,
-0.00200148,
-0.0121958,
-0.0153549,
-0.0176782,
-0.00832958,
-0.0214535,
-0.00518075,
-0.018216,
-0.00493571,
-0.00854786,
-0.012609,
-0.008941,
-0.0152265,
-0.0202135,
-0.0223379,
-0.0115268,
-0.0132236,
-0.0103302,
-0.0189098,
-0.0264375,
0.0182845,
-0.015093,
-0.00965085,
-0.006891,
-0.0115535,
0.0416656,
1.81344,
-2.05924,
0.404922,
0.167787,
-0.0241557,
0.0115943,
-0.00329233,
-0.0033552,
-0.00803268,
-0.0548073,
0.0167041,
0.00366971,
-0.00367776,
-0.0147465,
-1.41054,
-6.39367,
0.0962609,
-0.0245221,
-0.00225983,
-0.0135911,
-0.00952602,
-0.00737925,
0.00249597,
-0.00447351,
5.77133,
0.552828,
-0.119901,
0.0594778,
-0.0300833,
0.00209383,
-0.0127591,
0.00196444,
-0.00542456,
-0.000954198,
-0.00809888
]


# in1 = _load_hex_file("input.hex");
# in2 = in1[3179000:]
in3 = _load_hex_file("/mnt/overflow/work/software_parent_repo/higgs_sdr_rev2/libs/s-modem/soapy/productionjs/residue_upstream3.txt")
# # in3 = in3[3000000:]

in3res = _load_hex_file("/mnt/overflow/work/software_parent_repo/higgs_sdr_rev2/libs/s-modem/soapy/productionjs/save_residue3_strip.txt")

nplot(np.abs(in3), "in3");
nplot(np.abs(in3res), "in3res");

# for x in in3res:
# 	re = np.real(x)
# 	im = np.imag(x)

# 	mag2 = (re*re) + (im*im)
# 	if( mag2 < 2000):
# 		print(x)


# dump28 = _load_hex_file("/mnt/overflow/work/software_parent_repo/higgs_sdr_rev2/libs/s-modem/soapy/productionjs/dump29.hex");

# nplot(np.abs(dump28), "28")
# nplot(np.abs(in3res), "file")


# y1 = 187121672.0
# y2 = 187127447.0

# x1 = 5796.0
# x2 = 156.0


# slope = (x1-x2) / (y2-y1)

# print("slope", slope)


# nplotmulti([y],[x],["x"]);

# nplot(np.abs(in1), "in1 abs");

# nplot(in1)
# nplotqam(in2)
# nplot(np.abs(in2), "amp")

# nplot(np.abs(in3), "in3 real")

# nplot(np.abs(in3res), "in3 res")

nplotshow()