"""
    Copyright 2019 Samsung SDS
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import unittest
import pandas as pd
import numpy as np
from brightics.function.test_data import get_iris
from brightics.function.evaluation import plot_roc_pr_curve
import HtmlTestRunner
import os


class PlotROCPRCurveTest(unittest.TestCase):

    def setUp(self):
        print("*** Plot ROC PR Curve UnitTest Start ***")
        self.example_df = pd.DataFrame(np.array([[7.0, 3.2, 4.7, 1.4, 'versicolor', 'versicolor', 0.9470894443699033, 0.05291055563009675, -0.054361740023990725, -2.939152420701906, 0],
                                                 [6.4, 3.2, 4.5, 1.5, 'versicolor', 'versicolor', 0.8907919793072463, 0.10920802069275369, -0.11564434756037797, -2.2145007688012783, 1],
                                                 [6.9, 3.1, 4.9, 1.5, 'versicolor', 'versicolor', 0.8595247920559871, 0.14047520794401291, -0.15137560983295767, -1.962724261693012, 2],
                                                 [5.5, 2.3, 4.0, 1.3, 'versicolor', 'versicolor', 0.7168731193714991, 0.2831268806285009, -0.33285641447212727, -1.2618601403704282, 3],
                                                 [6.5, 2.8, 4.6, 1.5, 'versicolor', 'versicolor', 0.8036893475254762, 0.19631065247452384, -0.21854246814335726, -1.6280569128729305, 4],
                                                 [5.7, 2.8, 4.5, 1.3, 'versicolor', 'versicolor', 0.6904383915445347, 0.3095616084554653, -0.3704285330756914, -1.1725981486524766, 5],
                                                 [6.3, 3.3, 4.7, 1.6, 'versicolor', 'versicolor', 0.7911663559977391, 0.20883364400226093, -0.23424702233086292, -1.566217305674715, 6],
                                                 [4.9, 2.4, 3.3, 1.0, 'versicolor', 'versicolor', 0.9278067206414838, 0.0721932793585162, -0.07493184305903672, -2.6284083210929716, 7],
                                                 [6.6, 2.9, 4.6, 1.3, 'versicolor', 'versicolor', 0.9041962850967717, 0.0958037149032283, -0.10070881262733855, -2.345453817061664, 8],
                                                 [5.2, 2.7, 3.9, 1.4, 'versicolor', 'versicolor', 0.7352321631929386, 0.2647678368070614, -0.3075689613554737, -1.3289019245053981, 9],
                                                 [5.0, 2.0, 3.5, 1.0, 'versicolor', 'versicolor', 0.8344104583747928, 0.16558954162520725, -0.181029841367901, -1.7982431934624574, 10],
                                                 [5.9, 3.0, 4.2, 1.5, 'versicolor', 'versicolor', 0.8428527764556735, 0.15714722354432648, -0.17096297863337787, -1.850572183445849, 11],
                                                 [6.0, 2.2, 4.0, 1.0, 'versicolor', 'versicolor', 0.9165273628625352, 0.08347263713746483, -0.08716335632422902, -2.483236399782879, 12],
                                                 [6.1, 2.9, 4.7, 1.4, 'versicolor', 'versicolor', 0.7086297233512745, 0.2913702766487255, -0.34442214084388517, -1.233160392315393, 13],
                                                 [5.6, 2.9, 3.6, 1.3, 'versicolor', 'versicolor', 0.9528914711266131, 0.04710852887338686, -0.04825426310711688, -3.055301214238419, 14],
                                                 [6.7, 3.1, 4.4, 1.4, 'versicolor', 'versicolor', 0.9507435162854413, 0.04925648371455874, -0.05051095177583681, -3.0107142710024384, 15],
                                                 [5.6, 3.0, 4.5, 1.5, 'versicolor', 'versicolor', 0.6051028021902924, 0.39489719780970756, -0.5023569144105394, -0.9291298066637916, 16],
                                                 [5.8, 2.7, 4.1, 1.0, 'versicolor', 'versicolor', 0.929179913251592, 0.07082008674840798, -0.07345289556922484, -2.6476126073851507, 17],
                                                 [6.2, 2.2, 4.5, 1.5, 'versicolor', 'versicolor', 0.5559386103147119, 0.4440613896852881, -0.5870974039305662, -0.8117924610506891, 18],
                                                 [5.6, 2.5, 3.9, 1.1, 'versicolor', 'versicolor', 0.8970098398409725, 0.10299016015902748, -0.10868844726113054, -2.2731218277526417, 19],
                                                 [5.9, 3.2, 4.8, 1.8, 'versicolor', 'virginica', 0.4348096347353081, 0.5651903652646919, -0.8328469649757414, -0.5705926749117306, 20],
                                                 [6.1, 2.8, 4.0, 1.3, 'versicolor', 'versicolor', 0.9381698083480408, 0.0618301916519593, -0.06382431400630359, -2.783363495756763, 21],
                                                 [6.3, 2.5, 4.9, 1.5, 'versicolor', 'virginica', 0.46693215171467906, 0.5330678482853209, -0.7615713172757264, -0.6291065678232147, 22],
                                                 [6.1, 2.8, 4.7, 1.2, 'versicolor', 'versicolor', 0.7767319019448001, 0.22326809805519987, -0.2526600306974488, -1.49938199619454, 23],
                                                 [6.4, 2.9, 4.3, 1.3, 'versicolor', 'versicolor', 0.9336480590485045, 0.06635194095149557, -0.06865572220476088, -2.7127822654065343, 24],
                                                 [6.6, 3.0, 4.4, 1.4, 'versicolor', 'versicolor', 0.9331574705528629, 0.06684252944713703, -0.06918131364870728, -2.7054157326565464, 25],
                                                 [6.8, 2.8, 4.8, 1.4, 'versicolor', 'versicolor', 0.8433510306707923, 0.15664896932920774, -0.17037200116373333, -1.8537478410552604, 26],
                                                 [6.7, 3.0, 5.0, 1.7, 'versicolor', 'versicolor', 0.6361067843035493, 0.3638932156964507, -0.45238882988726903, -1.0108948178561665, 27],
                                                 [6.0, 2.9, 4.5, 1.5, 'versicolor', 'versicolor', 0.7223721227899655, 0.2776278772100345, -0.3252148673388507, -1.2814736331651126, 28],
                                                 [5.7, 2.6, 3.5, 1.0, 'versicolor', 'versicolor', 0.976608604202391, 0.023391395797609002, -0.023669317028457794, -3.7553870251939347, 29],
                                                 [5.5, 2.4, 3.8, 1.1, 'versicolor', 'versicolor', 0.889671069617619, 0.11032893038238098, -0.11690346926851322, -2.2042890989693156, 30],
                                                 [5.5, 2.4, 3.7, 1.0, 'versicolor', 'versicolor', 0.9302111669029236, 0.06978883309707636, -0.07234365742338564, -2.6622812662952344, 31],
                                                 [5.8, 2.7, 3.9, 1.2, 'versicolor', 'versicolor', 0.9280250344396733, 0.07197496556032666, -0.07469656979291356, -2.6314369209789525, 32],
                                                 [6.0, 2.7, 5.1, 1.6, 'versicolor', 'virginica', 0.2520978493792657, 0.7479021506207343, -1.377937975648666, -0.2904831242428088, 33],
                                                 [5.4, 3.0, 4.5, 1.5, 'versicolor', 'versicolor', 0.5213347834982588, 0.4786652165017412, -0.6513628649025827, -0.7367538476391291, 34],
                                                 [6.0, 3.4, 4.5, 1.6, 'versicolor', 'versicolor', 0.8126036622808582, 0.1873963377191418, -0.20751178857076327, -1.6745294519560643, 35],
                                                 [6.7, 3.1, 4.7, 1.5, 'versicolor', 'versicolor', 0.8769445871793008, 0.12305541282069925, -0.1313114731223703, -2.0951205143218212, 36],
                                                 [6.3, 2.3, 4.4, 1.3, 'versicolor', 'versicolor', 0.786985027409528, 0.21301497259047197, -0.23954605563830403, -1.546392821891228, 37],
                                                 [5.6, 3.0, 4.1, 1.3, 'versicolor', 'versicolor', 0.8727748369132394, 0.12722516308676055, -0.13607767517993183, -2.061796824631383, 38],
                                                 [5.5, 2.5, 4.0, 1.3, 'versicolor', 'versicolor', 0.7747901556767025, 0.22520984432329746, -0.25516305316152804, -1.490722669980643, 39],
                                                 [5.5, 2.6, 4.4, 1.2, 'versicolor', 'versicolor', 0.6585375428275679, 0.341462457172432, -0.41773374677769176, -1.074517541088001, 40],
                                                 [6.1, 3.0, 4.6, 1.4, 'versicolor', 'versicolor', 0.7839672697142441, 0.21603273028575581, -0.24338800731665755, -1.5323253536766253, 41],
                                                 [5.8, 2.6, 4.0, 1.2, 'versicolor', 'versicolor', 0.8962784524311231, 0.10372154756887689, -0.10950414148447875, -2.2660453977820585, 42],
                                                 [5.0, 2.3, 3.3, 1.0, 'versicolor', 'versicolor', 0.9289644151680999, 0.07103558483190005, -0.0736848453496184, -2.644574332681499, 43],
                                                 [5.6, 2.7, 4.2, 1.3, 'versicolor', 'versicolor', 0.7718812100990443, 0.22811878990095566, -0.2589246137257136, -1.4778887773678913, 44],
                                                 [5.7, 3.0, 4.2, 1.2, 'versicolor', 'versicolor', 0.8913997997577183, 0.10860020024228166, -0.11496224310767147, -2.2200820276324214, 45],
                                                 [5.7, 2.9, 4.2, 1.3, 'versicolor', 'versicolor', 0.8450392228131827, 0.1549607771868174, -0.16837223517182975, -1.864583244493177, 46],
                                                 [6.2, 2.9, 4.3, 1.3, 'versicolor', 'versicolor', 0.9091040934114608, 0.0908959065885392, -0.09529567715688186, -2.3980403108419477, 47],
                                                 [5.1, 2.5, 3.0, 1.1, 'versicolor', 'versicolor', 0.9716196923147926, 0.028380307685207405, -0.028790814135681842, -3.5620597656878896, 48],
                                                 [5.7, 2.8, 4.1, 1.3, 'versicolor', 'versicolor', 0.8569094017134697, 0.14309059828653029, -0.1544230815928693, -1.944277294881863, 49],
                                                 [6.3, 3.3, 6.0, 2.5, 'virginica', 'virginica', 0.015087560797893529, 0.9849124392021065, -4.193884662880208, -0.01520253597243214, 50],
                                                 [5.8, 2.7, 5.1, 1.9, 'virginica', 'virginica', 0.1001346599658115, 0.8998653400341885, -2.301239399188128, -0.10551014903657696, 51],
                                                 [7.1, 3.0, 5.9, 2.1, 'virginica', 'virginica', 0.1188313416212472, 0.8811686583787528, -2.13005008848687, -0.12650623166473404, 52],
                                                 [6.3, 2.9, 5.6, 1.8, 'virginica', 'virginica', 0.11766880980875583, 0.8823311901912442, -2.139881297210671, -0.12518779437443972, 53],
                                                 [6.5, 3.0, 5.8, 2.2, 'virginica', 'virginica', 0.0458083013795797, 0.9541916986204203, -3.0832899514570564, -0.04689068576985397, 54],
                                                 [7.6, 3.0, 6.6, 2.1, 'virginica', 'virginica', 0.05322480512165251, 0.9467751948783475, -2.933230729615544, -0.054693600588813965, 55],
                                                 [4.9, 2.5, 4.5, 1.7, 'virginica', 'virginica', 0.11448605522671285, 0.8855139447732872, -2.167302251817642, -0.12158707397439529, 56],
                                                 [7.3, 2.9, 6.3, 1.8, 'virginica', 'virginica', 0.11545097057100284, 0.8845490294289972, -2.1589093363654945, -0.12267733511643776, 57],
                                                 [6.7, 2.5, 5.8, 1.8, 'virginica', 'virginica', 0.0802552677866134, 0.9197447322133866, -2.5225428769255767, -0.08365911242503135, 58],
                                                 [7.2, 3.6, 6.1, 2.5, 'virginica', 'virginica', 0.0809468754205468, 0.9190531245794532, -2.5139621984848968, -0.08441135135547324, 59],
                                                 [6.5, 3.2, 5.1, 2.0, 'virginica', 'virginica', 0.3798620790951034, 0.6201379209048966, -0.9679470418936357, -0.4778133726096019, 60],
                                                 [6.4, 2.7, 5.3, 1.9, 'virginica', 'virginica', 0.1590349889989351, 0.8409650110010649, -1.838631044373731, -0.17320522391620108, 61],
                                                 [6.8, 3.0, 5.5, 2.1, 'virginica', 'virginica', 0.17829644230063957, 0.8217035576993604, -1.7243077077577709, -0.19637558437278044, 62],
                                                 [5.7, 2.5, 5.0, 2.0, 'virginica', 'virginica', 0.0640627251604392, 0.9359372748395608, -2.7478925949560473, -0.06620681881038576, 63],
                                                 [5.8, 2.8, 5.1, 2.4, 'virginica', 'virginica', 0.03487102623517346, 0.9651289737648265, -3.3560989884100763, -0.03549353500395803, 64],
                                                 [6.4, 3.2, 5.3, 2.3, 'virginica', 'virginica', 0.12768777250682006, 0.8723122274931799, -2.058167272236666, -0.13660786010919015, 65],
                                                 [6.5, 3.0, 5.5, 1.8, 'virginica', 'virginica', 0.21872490928010124, 0.7812750907198988, -1.5199404607568339, -0.24682796232576698, 66],
                                                 [7.7, 3.8, 6.7, 2.2, 'virginica', 'virginica', 0.12087452724169179, 0.8791254727583082, -2.1130022363502112, -0.12882764659404447, 67],
                                                 [7.7, 2.6, 6.9, 2.3, 'virginica', 'virginica', 0.010221548276502013, 0.989778451723498, -4.583257210915389, -0.010274147035236398, 68],
                                                 [6.0, 2.2, 5.0, 1.5, 'virginica', 'virginica', 0.20565912793834606, 0.7943408720616539, -1.581535199497648, -0.2302425999608032, 69],
                                                 [6.9, 3.2, 5.7, 2.3, 'virginica', 'virginica', 0.11346871692658766, 0.8865312830734123, -2.1762281018435257, -0.12043886579561033, 70],
                                                 [5.6, 2.8, 4.9, 2.0, 'virginica', 'virginica', 0.10474106381395454, 0.8952589361860455, -2.2562640334709507, -0.11064228837620457, 71],
                                                 [7.7, 2.8, 6.7, 2.0, 'virginica', 'virginica', 0.047169371741366706, 0.9528306282586333, -3.0540105008044156, -0.048318115930170255, 72],
                                                 [6.3, 2.7, 4.9, 1.8, 'virginica', 'virginica', 0.3559923535072482, 0.6440076464927518, -1.0328460272730058, -0.4400446795123222, 73],
                                                 [6.7, 3.3, 5.7, 2.1, 'virginica', 'virginica', 0.1502512862711396, 0.8497487137288604, -1.895446144730655, -0.162814604112429, 74],
                                                 [7.2, 3.2, 6.0, 1.8, 'virginica', 'virginica', 0.26769953817671355, 0.7323004618232865, -1.3178900536096771, -0.31156438226764493, 75],
                                                 [6.2, 2.8, 4.8, 1.8, 'virginica', 'virginica', 0.41016260765005486, 0.5898373923499451, -0.8912015938858473, -0.5279083862552703, 76],
                                                 [6.1, 3.0, 4.9, 1.8, 'virginica', 'virginica', 0.38358731200779916, 0.6164126879922008, -0.958188012620508, -0.4838385917243372, 77],
                                                 [6.4, 2.8, 5.6, 2.1, 'virginica', 'virginica', 0.059291186272891205, 0.9407088137271088, -2.825294613487116, -0.06112163071984765, 78],
                                                 [7.2, 3.0, 5.8, 1.6, 'virginica', 'virginica', 0.42365729302406685, 0.5763427069759332, -0.8588304217470967, -0.551052817826344, 79],
                                                 [7.4, 2.8, 6.1, 1.9, 'virginica', 'virginica', 0.14422813353816633, 0.8557718664618337, -1.9363589723415169, -0.1557514495035184, 80],
                                                 [7.9, 3.8, 6.4, 2.0, 'virginica', 'virginica', 0.4035325369214514, 0.5964674630785486, -0.9074981577908785, -0.5167305853215669, 81],
                                                 [6.4, 2.8, 5.6, 2.2, 'virginica', 'virginica', 0.04653917922350692, 0.9534608207764931, -3.067460757200186, -0.04765694468992154, 82],
                                                 [6.3, 2.8, 5.1, 1.5, 'virginica', 'virginica', 0.4584775465440075, 0.5415224534559925, -0.7798439600354555, -0.6133707481080617, 83],
                                                 [6.1, 2.6, 5.6, 1.4, 'virginica', 'virginica', 0.14265810008798896, 0.857341899912011, -1.9473044199835168, -0.15391849022133838, 84],
                                                 [7.7, 3.0, 6.1, 2.3, 'virginica', 'virginica', 0.12083973047698116, 0.8791602695230188, -2.1132901528784243, -0.12878806626431943, 85],
                                                 [6.3, 3.4, 5.6, 2.4, 'virginica', 'virginica', 0.05829977518955165, 0.9417002248104483, -2.8421570417300095, -0.06006828773783924, 86],
                                                 [6.4, 3.1, 5.5, 1.8, 'virginica', 'virginica', 0.21576387646915995, 0.78423612353084, -1.5335706337327124, -0.2430451260037003, 87],
                                                 [6.0, 3.0, 4.8, 1.8, 'virginica', 'virginica', 0.401764299751612, 0.598235700248388, -0.9118896813411728, -0.5137704551147, 88],
                                                 [6.9, 3.1, 5.4, 2.1, 'virginica', 'virginica', 0.27747081167438514, 0.7225291883256149, -1.2820395344831528, -0.3249974607449752, 89],
                                                 [6.7, 3.1, 5.6, 2.4, 'virginica', 'virginica', 0.07181359534644394, 0.9281864046535561, -2.633681470623426, -0.07452269928345467, 90],
                                                 [6.9, 3.1, 5.1, 2.3, 'virginica', 'virginica', 0.3257347268685217, 0.6742652731314783, -1.1216719501284886, -0.3941316651884791, 91],
                                                 [5.8, 2.7, 5.1, 1.9, 'virginica', 'virginica', 0.1001346599658115, 0.8998653400341885, -2.301239399188128, -0.10551014903657696, 92],
                                                 [6.8, 3.2, 5.9, 2.3, 'virginica', 'virginica', 0.06178476973044711, 0.9382152302695529, -2.784098389382073, -0.06377589971969803, 93],
                                                 [6.7, 3.3, 5.7, 2.5, 'virginica', 'virginica', 0.05979618239721041, 0.9402038176027896, -2.816813459574911, -0.0616585999847052, 94],
                                                 [6.7, 3.0, 5.2, 2.3, 'virginica', 'virginica', 0.18707621040024358, 0.8129237895997564, -1.6762392029030442, -0.2071179135578664, 95],
                                                 [6.3, 2.5, 5.0, 1.9, 'virginica', 'virginica', 0.1975133221838481, 0.8024866778161519, -1.6219492428204523, -0.22004002496790895, 96],
                                                 [6.5, 3.0, 5.2, 2.0, 'virginica', 'virginica', 0.26045390613122266, 0.7395460938687773, -1.3453293772792005, -0.3017186676462986, 97],
                                                 [6.2, 3.4, 5.4, 2.3, 'virginica', 'virginica', 0.099453949861257, 0.900546050138743, -2.308060557414477, -0.10475397726305277, 98],
                                                 [5.9, 3.0, 5.1, 1.8, 'virginica', 'virginica', 0.21255820012039828, 0.7874417998796017, -1.5485394451972243, -0.23896581592824317, 99]]),
                                                 columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species', 'prediction', 'probability_0', 'probability_1', 'log_probability_0', 'log_probability_1', '__index_level_0__'])
        self.example_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'probability_0', 'probability_1', 'log_probability_0', 'log_probability_1', '__index_level_0__']] = self.example_df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'probability_0', 'probability_1', 'log_probability_0', 'log_probability_1', '__index_level_0__']].astype(float)

    def tearDown(self):
        print("***  Plot ROC PR Curve UnitTest End ***")

    def test_plot_roc_pr_curve1(self):
        plot_roc_pr_curve_out = plot_roc_pr_curve(table=self.example_df, label_col='species', probability_col='probability_0', fig_w=6.4, fig_h=4.8, pos_label='versicolor', group_by=None)

    def test_plot_roc_pr_curve2(self):
        plot_roc_pr_curve_out = plot_roc_pr_curve(table=self.example_df, label_col='species', probability_col='probability_0', fig_w=6.4, fig_h=4.8, pos_label='versicolor', group_by=['species'])


if __name__ == '__main__':
    filepath = os.path.dirname(os.path.abspath(__file__))
    reportFoler = filepath + "/../../../../../../../reports"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, output=reportFoler))