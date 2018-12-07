import matplotlib.pyplot as plot
import numpy as np

# This is what fft looks like for a 1 at 17000 hz
fft1 = [1.6355272691725986e-06, 8.78624359756941e-06, 9.91302149486728e-05, 1.3690962077816948e-05, 5.2007235353812575e-06, 1.404122713211109e-06, 1.2684512995519981e-08, 4.71083666298e-07, 1.4440415441185905e-07, 3.4009931937362126e-07, 2.311227262907778e-07, 2.5099100753323e-07, 1.752694629431062e-07, 2.2251832376696257e-07, 3.5442852208689146e-08, 8.660335737431524e-08, 1.741119177722794e-07, 6.923377782186435e-08, 2.45384779162805e-08, 2.906889617904085e-09, 7.41811234661327e-08, 7.076562269503484e-08, 4.464707714646465e-08, 9.312703497244001e-08, 2.7361704013628696e-08, 5.009268022604374e-08, 3.024728201239668e-08, 7.618342401372047e-09, 5.248277901159781e-08, 1.0684369300406615e-07, 3.260407765992568e-08, 2.800881837572433e-08, 9.369320252972102e-08, 2.018626048538863e-07, 1.2951957728546404e-07, 1.2386810688269634e-08, 2.455624326103134e-08, 2.33325962994968e-08, 8.471671364418398e-09, 3.7371589201029565e-07, 1.5157554855704802e-07, 7.651537003994235e-08, 3.650196589433108e-08, 1.8350378638842813e-07, 1.135571991994766e-07, 1.8695706671678636e-07, 2.984516100923429e-08, 1.6548476367006515e-07, 2.4776209528454274e-08, 3.271595403475658e-07, 1.5917810003429622e-07, 6.013215880784628e-08, 1.708384189669232e-07, 5.038190664663489e-08, 8.046749400136832e-08, 8.631946002424229e-08, 1.1639805563845584e-07, 1.6564944971264595e-08, 6.98715467706279e-08, 8.06381166285064e-08, 1.1915735065315403e-08, 3.23899342902223e-08, 5.0997268630226245e-08, 5.315627760182906e-08, 4.820924459636444e-08, 2.130412735112941e-09, 5.113844636639442e-08, 3.422570316047313e-08, 3.2123857351962215e-08, 2.2477527394926256e-08, 6.34539887300889e-08, 1.1086207507560175e-08, 1.4209138754495143e-08, 3.7074734393627296e-08, 6.415885422939027e-08, 2.8619919767436386e-09, 1.2764381551733095e-08, 6.451398348872317e-08, 6.422418152851606e-08, 3.913876867045474e-08, 4.9493131371036725e-08, 1.107864022742433e-08, 1.6595649299233628e-07, 3.069443810232997e-09, 1.611483502195199e-09, 6.581757805435018e-09, 3.0236435577535303e-08, 3.929757497189712e-08, 1.2573723395803427e-08, 1.1729271776061978e-08, 7.0125305562385165e-09, 5.219022103375437e-09, 2.033456780736742e-08, 3.163563633279409e-08, 5.504487088359156e-09, 1.2909167068642091e-08, 6.5264198489956016e-09, 2.3675625016039703e-08, 2.109514340986607e-08, 1.0762387425700126e-08, 1.6210099929026e-09, 2.0090055841137655e-08, 5.876595654541461e-09, 2.5468617437240937e-08, 1.2493233114696523e-08, 1.9203630685638018e-08, 1.3550074395851652e-09, 2.66085606881461e-08, 2.5396923675202743e-08, 4.958673915922418e-09, 6.979751443481064e-09, 2.103838880884723e-09, 9.560698899235831e-09, 3.4699401130211527e-09, 4.106300188766454e-09, 2.1918816983657052e-08, 1.842483854375132e-08, 5.2474419476311596e-08, 6.328687618406548e-08, 2.6374554096264546e-08, 2.314881264453561e-08, 4.672222608803622e-09, 2.247647623576654e-09, 1.7675956698326445e-08, 1.4506213119602762e-08, 3.1898128582952268e-09, 2.627710049551979e-09, 8.629840841933856e-09, 8.95264040678967e-09, 2.635390039529284e-08, 3.185553865137081e-08, 6.574989441787693e-09, 2.3296038431652732e-09, 1.3864813297459477e-08, 3.8442923511183835e-08, 6.890929160618953e-09, 3.4166987017414385e-09, 4.05844957640511e-09, 5.031561389756689e-09, 3.4191367515035154e-09, 2.029019974258972e-08, 2.0694777003171794e-09, 1.725062537261124e-09, 3.627911482340096e-08, 1.6751352527322183e-09, 3.08716323615954e-08, 7.396925294500534e-09, 1.199461863166107e-09, 6.387879558644727e-09, 2.0401560441030142e-09, 1.2362557200162883e-08, 9.090417307788812e-09, 1.579470065848909e-08, 2.422025247028614e-09, 3.03877314422607e-08, 7.586147710014757e-09, 2.2419099909853912e-09, 2.0840813519384938e-08, 7.619186948026879e-10, 2.491791839531743e-08, 6.195207902237598e-09, 3.0959153018983443e-09, 8.617548452605206e-09, 2.263514486955387e-09, 7.279624458789158e-09, 8.058866463045433e-09, 7.01862123975161e-10, 7.376514954415825e-09, 4.629925776100663e-09, 9.470147332990564e-09, 2.3054789188847735e-09, 3.0632458791757244e-09, 2.9210927010581145e-09, 7.577563465588355e-09, 5.388396839833831e-09, 7.758265141433185e-09, 1.4260645997410393e-08, 1.4918971613653298e-09, 1.5721941082347257e-08, 1.6903548782920552e-08, 8.195678802280781e-09, 3.910354262615101e-09, 7.241937050039837e-10, 1.4640813006394637e-08, 7.474248775451997e-09, 3.6085832100241078e-09, 2.052415837283661e-08, 6.044834410801059e-09, 1.5850460943767075e-09, 1.4220654875884975e-08, 8.3051503452225e-09, 2.0994779248439954e-09, 4.5068540011072855e-09, 5.65120350515258e-09, 7.209635111138368e-09, 5.78416026186801e-09, 1.1288014967192339e-08, 9.541711420979482e-09, 1.0809146466783659e-08, 8.949808005809246e-09, 4.253311036706009e-09, 2.8878341939986285e-09, 4.0949816870750055e-09, 3.6403888792335692e-09, 1.3051165481670068e-08, 7.899982890080537e-09, 3.075382171147112e-09, 1.2852537700780431e-08, 1.3107855245664268e-08, 1.706334273876564e-08, 1.1928294796348382e-08, 8.641682036625298e-09, 8.813044516386981e-09, 1.3705618862047686e-09, 1.3065520221289262e-08, 1.0924930293754187e-08, 4.185650936960883e-09, 1.3237731799620178e-08, 1.2017911998896125e-08, 8.449138277910606e-09, 1.1319833070899676e-08, 1.8314850080969336e-08, 9.41622513295215e-09, 8.255958139358199e-10, 5.108014455856846e-09, 1.8614001451311424e-09, 1.2058870346720596e-08, 6.752711723123639e-09, 7.825993186827418e-09, 8.569484677423134e-09, 1.47918006732084e-08, 1.0232904301687995e-08, 1.0056775856526201e-08, 5.3778572706164596e-09, 1.359933587963269e-08, 7.09678360522048e-09, 1.4402715464711946e-08, 1.2899981527425552e-08, 1.1686950074363267e-08, 7.752250397174976e-09, 1.0737999822652e-08, 1.9048709276603404e-09, 1.1827209434045471e-08, 8.00512012233412e-09, 9.582254101303533e-09, 1.0845659481617531e-08, 1.208868383173467e-08, 1.1111149333942194e-08, 1.8030403836633013e-08, 1.8406172586082903e-08, 5.40329869735956e-09, 9.90782744736407e-09, 1.024254281389858e-08, 1.305160335363098e-08, 7.637359189516246e-09, 1.7923563078170446e-08, 1.8253398792467124e-08, 1.3740325321975888e-08, 6.871852864520633e-09, 9.946961476714478e-09, 1.4483485522021056e-08, 1.3520599750904694e-08, 1.037363439593264e-08, 1.7615683134408755e-08, 1.1169675850908334e-08, 1.4859542929457348e-08, 1.736157706488939e-08, 9.639440357034346e-09, 1.269955962612812e-08, 1.51499417455625e-08, 2.6962862165191837e-08, 1.3473761661941808e-08, 2.277201360811887e-08, 1.2103102520200082e-08, 1.5814187293017312e-08, 1.968779095307127e-08, 1.4633403822017499e-08, 9.582873161662064e-09, 1.564806417775344e-08, 2.1800815375172533e-08, 1.9486222413434007e-08, 1.9524733829712204e-08, 1.9746568824530186e-08, 2.1215575074506887e-08, 2.24983676133661e-08, 1.583785724790232e-08, 3.016011973500099e-08, 2.3425013040423437e-08, 1.736148114162006e-08, 1.8845309313064718e-08, 2.996577208591589e-08, 2.3306336416339946e-08, 2.1554621199015855e-08, 2.4210841331751e-08, 2.236697582702618e-08, 2.3809725746559707e-08, 1.8492622544385995e-08, 2.8362830306605247e-08, 2.4952075960982256e-08, 2.672143573079211e-08, 3.167700057815637e-08, 2.659185405207154e-08, 3.496334599617512e-08, 2.947537325326266e-08, 3.363043887816275e-08, 2.472637206096806e-08, 3.5056903158192654e-08, 3.5853449986689157e-08, 3.00613436365893e-08, 3.501025602759e-08, 3.845993390427793e-08, 3.5573890500018024e-08, 3.359060585239604e-08, 3.90695795715601e-08, 3.831875616810976e-08, 4.378335916044307e-08, 4.475942105841568e-08, 4.0717523575040104e-08, 3.790984592910718e-08, 5.463778052217094e-08, 5.1980180160171585e-08, 4.9166590798677134e-08, 4.024593280860245e-08, 4.742715731254066e-08, 5.801732427812567e-08, 6.08859522799321e-08, 5.378477752060462e-08, 5.752763954092188e-08, 5.2405340511541e-08, 6.745975866806475e-08, 7.56503055754365e-08, 4.578416223921522e-08, 6.338063229804902e-08, 7.154992687219419e-08, 8.237862658688755e-08, 7.392246459403395e-08, 8.791013783593371e-08, 7.666130841244012e-08, 7.940692370311808e-08, 7.548543834445809e-08, 8.202800927392673e-08, 8.124309403001462e-08, 9.440197601406908e-08, 9.775387610488906e-08, 9.759977359635741e-08, 1.2072405297658406e-07, 1.0359809010651588e-07, 1.1197063543022523e-07, 1.1779911091025497e-07, 1.3132122944625735e-07, 1.3997316727909492e-07, 1.359255605848375e-07, 1.3491683148458833e-07, 1.3416739363947272e-07, 1.6824810700200032e-07, 1.6747559072882723e-07, 1.442467834067429e-07, 1.7847072797394503e-07, 1.9523611172189703e-07, 2.1355424451030558e-07, 2.0068873141099175e-07, 2.0174690007479512e-07, 2.0660800714722427e-07, 2.5060359121198417e-07, 2.6787620299728587e-07, 2.7030134219785396e-07, 2.521948658795736e-07, 3.072435958983988e-07, 3.120397025213606e-07, 3.4476789778636885e-07, 3.919892606063513e-07, 3.652844782209286e-07, 3.7790883311572543e-07, 4.4702042600874847e-07, 4.817828198611096e-07, 5.471240456245141e-07, 5.119781576468085e-07, 5.956355266789615e-07, 6.201934183991398e-07, 6.88076113419811e-07, 7.653162583665107e-07, 8.323181077685149e-07, 9.044769058164093e-07, 1.006136244541267e-06, 1.0814833331096452e-06, 1.197172991851403e-06, 1.3494932318280917e-06, 1.4782276593905408e-06, 1.6805719269541441e-06, 1.8204840444013826e-06, 2.5983686100516934e-06, 2.5451768124185037e-06, 2.8930733151355525e-06, 3.302655159131973e-06, 4.223436462780228e-06, 4.696074029197916e-06, 6.342610504361801e-06, 6.8409376581257675e-06, 9.663571290730033e-06, 1.3188507182348985e-05, 1.629445978323929e-05, 2.8600494260899723e-05, 4.2768733692355454e-05, 8.610760414740071e-05, 0.00020107686577830464, 0.0012258070055395365, 0.007855972275137901, 0.00037072142004035413, 0.00012737912766169757, 5.979677371215075e-05, 3.395259045646526e-05, 2.263253554701805e-05, 1.669098128331825e-05, 1.0393205229775049e-05, 9.101184332394041e-06, 8.006430107343476e-06, 7.164159342210041e-06, 5.315041107678553e-06, 4.64438699054881e-06, 3.98111660615541e-06, 3.5992641187476693e-06, 3.0914281978766667e-06, 2.3975305794010637e-06, 2.3058837541611865e-06, 2.0815839434362715e-06, 1.9745259578485275e-06, 1.7992455241255811e-06, 1.6387411960749887e-06, 1.474817622693081e-06, 1.404809154337272e-06, 1.2680428653766285e-06, 1.1890390396729345e-06, 1.0931184988294262e-06, 1.0033593298430787e-06, 9.556374607200269e-07, 9.138805125985527e-07, 9.668400480222772e-07, 8.368915018763801e-07, 7.906988344075216e-07, 7.845241611903475e-07, 7.049928854030441e-07, 6.859467589492851e-07, 6.701775987494329e-07, 6.7320655716685e-07, 6.245592203413253e-07, 5.822241178066179e-07, 5.617279725811386e-07, 5.532687623599486e-07, 5.310945994096983e-07, 4.937937205795606e-07, 5.038239692112256e-07, 4.825713517675467e-07, 4.684453358549945e-07, 4.256207830621861e-07, 4.385545082641329e-07, 4.175846868292865e-07, 3.976331868216221e-07, 3.9949941310624126e-07, 3.875440768297267e-07, 3.6237469203115324e-07, 3.7975510736032447e-07, 3.6090415278522414e-07, 3.6127781299910566e-07, 3.485660613478103e-07, 3.2726597964938264e-07, 3.1804464128981635e-07, 3.193553652636183e-07, 3.1143503065322875e-07, 3.061606435039721e-07, 2.997988701736176e-07, 2.9422429292935703e-07, 2.89730280655931e-07, 2.832620111803408e-07, 2.72825531055787e-07, 2.6813438580575166e-07, 2.888461665406794e-07, 2.678372652553662e-07, 2.662243616669002e-07, 2.571360369074682e-07, 2.5819258553383406e-07, 2.5029453354363795e-07, 2.513191930120229e-07, 2.4948124632828694e-07, 2.4390823227804503e-07, 2.385426114415168e-07, 2.3067651966357516e-07, 2.3794029857526766e-07, 2.3214265354454255e-07, 2.2929945941996266e-07, 2.2337515304116096e-07, 2.2721805237324588e-07, 2.2321017922877218e-07, 2.2477493644146307e-07, 2.2195912663391937e-07, 2.1670302885468118e-07, 2.2333782112582412e-07, 2.1981074382892984e-07, 2.2343603234276088e-07, 2.1925856685811596e-07, 2.161732055583343e-07, 2.1957012563689204e-07, 2.1040708020336751e-07, 2.1003599215418944e-07, 2.1141359241028113e-07, 2.0903624431412027e-07, 2.0761211771969101e-07, 2.1175866038447566e-07, 2.087968766772974e-07, 2.149388791394813e-07, 2.0272939593724004e-07, 2.121114022202164e-07, 2.1293311647241353e-07]
frequency = range(0, len(fft1))
# Each bin is a range of 43 hz
for i in range(len(frequency)):
    frequency[i] *= 43

plot.scatter(frequency, fft1)
plot.show()

# This is what fft looks like for a 0 at 15000 hz
fft0 = [8.5866340668872e-06, 1.4017617104400415e-05, 1.6036316083045676e-05, 4.147248910157941e-05, 7.724451620561013e-07, 7.612839908688329e-06, 1.5588987025694223e-06, 3.0183284707163693e-06, 1.0951363265121472e-06, 1.6335483223883784e-06, 1.9678257956456946e-07, 4.2552020573793925e-08, 2.596571846424922e-07, 4.7602501496157856e-08, 6.805030494660969e-08, 2.7266253255220363e-07, 5.668151459303772e-08, 1.1892459461648741e-08, 3.790830405137058e-08, 4.1373738213223987e-07, 3.612346404224809e-07, 3.209852934560331e-07, 1.713518145152193e-07, 1.1876326588833308e-08, 1.6342991671081109e-07, 5.3455202930763335e-08, 3.5566241507467566e-08, 4.290806998596963e-07, 5.361545518667299e-08, 2.1113629955493707e-08, 2.2430228341363545e-07, 8.22774310904606e-08, 2.0318029925192604e-08, 2.3781858260463196e-07, 7.125228762561164e-08, 1.4746335352811002e-07, 1.3848573132690944e-07, 3.4658626191230724e-08, 1.9185414146249968e-07, 1.0527225668965912e-07, 1.1419171386251037e-07, 3.0010318141648895e-07, 1.6336315411535907e-07, 2.5431913286411145e-07, 6.782859145459952e-07, 2.150553335411587e-08, 4.405715259281351e-08, 3.4427395689817786e-07, 2.127453946343394e-08, 2.4039638901740545e-07, 3.9219307268467674e-07, 2.0548691637145566e-08, 3.807260213761765e-07, 5.412751420408313e-07, 3.811152566868259e-07, 2.076397720429668e-08, 3.2814586603535645e-08, 7.011712455096131e-08, 8.170783871719323e-08, 5.394625191001978e-09, 1.25872134049132e-07, 5.83958268407514e-08, 3.31403771092198e-09, 1.9270345319455373e-09, 1.8387693145882622e-08, 3.1776874465094807e-08, 3.019661676262331e-08, 2.8270565888277588e-09, 8.213691415903668e-08, 1.2521708470103476e-07, 1.8406448987207114e-07, 3.079921739868041e-08, 9.864100647405394e-09, 4.111545326423993e-09, 3.624641067290213e-07, 8.466995993217097e-09, 5.808387726347064e-08, 3.481108379332909e-08, 7.513776267842331e-09, 1.3999303405398678e-07, 7.793074274786704e-08, 4.616392246248324e-08, 4.745001547235006e-08, 1.4561892669462395e-07, 1.4946377291380486e-07, 3.865453734874791e-08, 8.995120737154139e-08, 8.116693983595269e-09, 2.347132621594028e-08, 8.167376108758617e-08, 3.742194465417015e-08, 1.1319731640924147e-07, 1.5834420707960817e-07, 8.444951760111508e-08, 1.7989970046983217e-07, 8.895057135305251e-09, 9.585397364730852e-09, 3.132912951286926e-08, 3.288923977606828e-08, 1.034338552585723e-07, 2.903160600808974e-09, 4.376348883283754e-08, 6.887867609606246e-09, 2.1613347556126428e-08, 1.1984265135822625e-08, 4.232476591425893e-09, 1.0182733767294394e-08, 1.0816409101721547e-08, 1.612312616749989e-09, 2.3696786755067478e-08, 5.271612923962721e-09, 1.4266673176166478e-08, 1.0565496255665607e-09, 1.767783608386253e-08, 4.028788858079224e-09, 1.0352058765761285e-08, 3.7341802539003766e-08, 1.6019431114955296e-08, 2.5142501414165963e-08, 1.185825482252767e-08, 1.0819939610939855e-08, 6.4504224184247505e-09, 4.205722436978476e-09, 7.765593723618736e-10, 7.473963670179273e-09, 7.824199066419624e-09, 1.8132348955646194e-08, 1.4757775446128107e-08, 5.512804879259647e-09, 1.3450986102725437e-08, 1.6248659084894257e-09, 4.7291188742804025e-09, 2.219078254483975e-08, 2.3748503164000567e-09, 2.1457356780274495e-08, 9.649930632349424e-09, 1.1752774753404083e-08, 1.2850124520014106e-08, 2.2430590718158783e-08, 7.17490400425902e-10, 8.303234544371207e-09, 5.272734249217592e-09, 1.3290339939686646e-09, 2.222285688802117e-09, 2.722506442509598e-09, 1.67529492500762e-08, 1.4222527155993703e-08, 5.071119968391713e-09, 1.1708251257402935e-08, 7.102305854544966e-09, 2.8526565998276965e-08, 6.01667622390778e-08, 4.980287293676611e-09, 6.907429628277839e-10, 4.794405150665426e-11, 9.802940681424843e-09, 1.352976308766074e-08, 2.415467270644456e-10, 1.3977510704421547e-08, 6.073462621714043e-09, 2.0414592238893192e-09, 3.3150611145060793e-09, 4.176962664637074e-10, 8.560659736644993e-09, 4.145745968742176e-09, 9.550664259450059e-09, 2.240933216768326e-09, 5.496402444293835e-09, 1.4884116161795191e-08, 7.91587184689746e-10, 4.2126596655478465e-10, 1.3298174117437611e-08, 7.788534261976565e-09, 9.205114448462837e-10, 5.164150218561758e-10, 3.43392841939405e-10, 1.651582337558466e-08, 3.2900275837022264e-09, 1.7911265359771278e-08, 8.236207549305874e-11, 8.05826849692437e-10, 3.4334803888924625e-09, 9.593038585720137e-10, 1.575532926345602e-09, 1.659577919532751e-09, 2.0836717767869217e-13, 5.078477083308996e-10, 2.590234027266547e-09, 7.361113940618225e-10, 1.268000038301409e-09, 1.132106852708148e-09, 2.9406441726109733e-09, 1.3721545011335934e-09, 2.9868487683160083e-09, 8.650078986427445e-10, 4.623209037823983e-10, 1.954895689770808e-10, 1.6754045928379924e-09, 2.2111661390766812e-09, 5.298673499964934e-09, 2.6658502072507417e-09, 3.4156346639946378e-09, 4.005090925573995e-09, 7.91071097516749e-11, 1.2900086554523682e-10, 1.2821629313819471e-09, 7.870882279270575e-10, 3.6292899796563916e-09, 6.085294490532078e-09, 1.8268286883227347e-09, 1.449765862915342e-10, 2.6975390809980127e-09, 2.238844887259006e-09, 2.3119000047699956e-09, 9.765344088918937e-10, 9.816329971101823e-10, 7.871586937824304e-09, 2.7756252851673935e-09, 8.224982472881948e-09, 2.2846990965774694e-09, 3.665834025223802e-10, 4.2619946460931146e-10, 6.017349951648043e-10, 3.2448388420647234e-10, 3.0206450674086227e-09, 1.4640001433363636e-09, 7.902029031114921e-11, 2.100200915955419e-11, 1.4850093377205553e-09, 5.966477978347484e-09, 1.5839690670205187e-09, 1.9528132444435187e-09, 3.925746838717714e-09, 1.051004505647768e-09, 1.2507984648024717e-09, 3.017729843790562e-09, 1.260913817802134e-09, 3.901339251655145e-09, 5.926966695213309e-10, 2.0298307479293953e-09, 2.505694318699625e-09, 1.6633206811889067e-08, 7.703770954492484e-09, 1.675716787552517e-09, 5.271498237924277e-10, 1.1459269089186819e-09, 3.6074967457722096e-09, 2.5745681142552712e-09, 2.6082527804227595e-10, 5.7970450662026e-10, 9.560298330768546e-09, 3.1744704087621756e-10, 1.129712642877756e-11, 5.182878015652648e-10, 1.2605434751566946e-10, 2.2542591057717054e-11, 1.5430480504452504e-10, 1.5233795336300204e-09, 4.1130630151764436e-11, 1.799410898062348e-10, 8.525792849489733e-10, 2.1341630684901247e-09, 1.360278889528388e-09, 3.3499651941326647e-09, 1.3449715785540661e-09, 3.3675240374009263e-10, 1.3169733081852542e-09, 4.0965469905174245e-10, 5.140880499077127e-10, 3.102673118426935e-10, 1.6518417744748604e-09, 2.7208131303524397e-09, 4.821198301696583e-11, 1.4609685683453222e-09, 3.816653659782787e-10, 3.771430112653462e-10, 2.60260230033893e-10, 3.9086001102361934e-10, 3.3316507885849944e-10, 1.3378501084737593e-10, 1.420004225316518e-09, 5.439819705799209e-10, 7.007094904309952e-10, 1.5188907909191585e-09, 4.688481158865443e-09, 4.3805795102436207e-10, 2.932463993854384e-10, 8.381457333728193e-11, 1.3884784433315644e-09, 6.544255692908507e-10, 1.45302225806887e-09, 2.211483662861724e-09, 5.54316426093493e-10, 1.220915923916266e-09, 3.151983785087964e-09, 2.7260798063366565e-09, 1.7382330019799497e-09, 8.474270174474441e-10, 8.383795879751688e-10, 2.64601052180069e-09, 2.179907143684545e-09, 1.4536033487999589e-09, 3.6675980030764777e-09, 2.8271811558511217e-09, 2.520861297483634e-09, 5.568659977583934e-10, 2.1658399518287297e-09, 2.9711297866441555e-09, 7.141537916588447e-10, 2.2421053902377253e-09, 3.9091800907442575e-09, 1.9744585966208206e-09, 5.745107500843005e-09, 4.426513378064101e-09, 3.940473281005552e-09, 3.787465452376182e-09, 7.576444360779533e-09, 4.418527765892577e-09, 6.4697722734763374e-09, 6.735811020064375e-09, 4.0523078226328835e-09, 7.76230812959966e-09, 6.946968778009932e-09, 7.0600649770824475e-09, 1.367412227892828e-08, 9.422601365827177e-09, 1.63685598408847e-08, 1.6538672653609865e-08, 1.8244870503281163e-08, 1.1644136321820042e-08, 1.5053196023018245e-08, 1.8591926220778987e-08, 1.9243236337729286e-08, 2.260178888491282e-08, 3.0146800611419167e-08, 3.6932593872052166e-08, 3.453159536093153e-08, 4.621902505164144e-08, 4.768711292513217e-08, 5.31057438024618e-08, 6.524307849531397e-08, 7.342667629472999e-08, 1.3063815629266173e-07, 1.559855462573978e-07, 5.42864256658504e-07, 5.128660518494144e-07, 6.130071596999187e-07, 1.1697079571604263e-06, 2.5238593934773235e-06, 1.2461593541956972e-05, 0.001021797419525683, 8.624817382951733e-06, 2.1672747152479133e-06, 1.2520143854999333e-06, 5.758448651249637e-07, 6.136593242445088e-07, 1.3285730915413296e-07, 2.3988971520338964e-07, 2.0105366616007814e-07, 1.282753316900198e-07, 1.2346883693226118e-07, 1.0346342804723463e-07, 9.358648611623721e-08, 7.476398167227671e-08, 6.276872710486714e-08, 6.437897326350139e-08, 4.857195889940158e-08, 4.540739340086475e-08, 3.2395639948390453e-08, 2.7433257443476577e-08, 2.6544562103936187e-08, 2.5841867312692557e-08, 3.146537252973758e-08, 2.0185220606094845e-08, 2.539464993844831e-08, 1.862514942274629e-08, 1.5317176860207837e-08, 1.8179830973963362e-08, 1.800597360102074e-08, 1.4609566889589587e-08, 1.4348520593898684e-08, 1.4452636420969611e-08, 1.4111715351816656e-08, 1.2744598265612694e-08, 1.143409011916674e-08, 1.763320334191576e-08, 1.071602184765652e-08, 9.382671528612718e-09, 5.795322444157591e-09, 1.7040578725868727e-08, 8.488277636331532e-09, 9.406345924389825e-09, 8.099044102038988e-09, 9.399885314564926e-09, 1.0917026393997276e-08, 6.587301371041576e-09, 5.958834314867545e-09, 6.752637116136384e-09, 5.568299599190141e-09, 1.0304809450190078e-08, 5.298779193196879e-09, 4.821583132752494e-09, 9.445916049344305e-09, 5.666522362446358e-09, 8.165611298238673e-09, 3.6483338572423918e-09, 4.765610128742992e-09, 9.107889553661153e-09, 4.548160514872279e-09, 1.1807182787038073e-08, 4.058234637227542e-09, 3.738351406212814e-09, 4.053328783726329e-09, 6.041850575400076e-09, 6.728344548179166e-09, 5.780985912196002e-09, 3.4240374979788157e-09, 5.436632477540115e-09, 4.39997815959714e-09, 3.766682521444409e-09, 3.8398320079124915e-09, 5.171655104163619e-09, 5.172557493438035e-09, 4.726146141109666e-09, 3.5781784202271183e-09, 5.8867120067418455e-09, 4.814975529399135e-09, 3.2226075141750243e-09, 3.1079669948752553e-09, 3.6970959627069533e-09, 3.205243181980677e-09, 4.451349955303385e-09, 4.50023485143447e-09, 3.960025640736831e-09, 2.8353026593208597e-09, 4.622536575737968e-09, 2.1387598359012827e-09, 1.6025886173665072e-09, 6.815545905425324e-09, 9.970093639566358e-10, 6.96113122700126e-09, 2.175710278606857e-09, 7.25873627871465e-09, 2.6622757332006586e-09, 1.4393518599220556e-09, 5.046350004533906e-09, 2.455550873747825e-09, 4.878974557698257e-09, 5.419596327271847e-09, 2.326520975870494e-09, 3.844222717930279e-09, 4.45486048050725e-09, 1.5833158117928292e-09, 4.473306169927582e-09, 1.7560360943136288e-09, 2.888700612047046e-09, 3.2806566352405753e-09, 4.8820467668519996e-09, 3.507119039625195e-09, 2.5532984615495025e-09, 3.4445462038235064e-09, 2.9627509334773094e-09, 2.2120947296144777e-09, 3.0048323829134915e-09, 2.543054433701286e-09, 1.8463062190221535e-09, 1.7514799610651721e-09, 2.06330019736356e-09, 2.8403199792137457e-09, 3.0005815609968067e-09, 2.222058093082069e-09, 2.986326075316015e-09, 2.79183720586218e-09, 2.447710700792527e-09, 2.3611355093322572e-09, 2.9704454451717766e-09, 2.4718336266715824e-09, 2.8711020227945028e-09, 1.7010680641860176e-09, 1.9637815817930004e-09, 3.2375617742275153e-09, 1.8028305515116472e-09, 2.1598776100972827e-09, 2.282019240240629e-09, 2.5049262664111893e-09, 2.348018446340916e-09, 2.561340695095282e-09, 2.3673840665594525e-09, 2.2755910489280495e-09, 2.57445353923913e-09, 2.688673061967961e-09, 2.437181789716192e-09, 2.7160274029824905e-09, 2.415761368723679e-09, 2.391127296164086e-09, 2.336890903009703e-09, 2.5320614494006577e-09, 2.3809110238914855e-09, 2.4644082330382844e-09, 2.4242934326679233e-09, 1.9579025067884004e-09, 2.123274667198416e-09, 2.487988925992113e-09, 2.133288878880535e-09, 2.2629522700157167e-09, 2.140456478727515e-09, 2.259643139268519e-09, 2.4563959755141695e-09, 1.9633779047012467e-09, 2.0439934189653286e-09, 2.172846125247929e-09, 2.165094992179206e-09]
frequency = range(0, len(fft0))
for i in range(len(frequency)):
    frequency[i] *= 43

print np.argmax(fft1)*43, np.argmax(fft0)*43
plot.scatter(frequency, fft0)
plot.show()

# Used this to generate sample
preamble = [1, 0, 1];
header = [0, 0, 1];
data = [1, 0, 1, 1, 1, 0, 1, 0];

# Sample Frequencies
dataarray = [17070.22265625, 15068.7646484375, 17209.244140625, 15208.7880859375, 15209.1748046875, 17308.837890625, 17308.76953125, 14808.3720703125, 17108.91015625, 17108.265625, 17108.45703125, 14909.0224609375, 16809.333984375, 15109.2236328125]
time = range(0, len(dataarray))

# Plot frequencies with the mean as a threshold for 0 and 1
plot.scatter(time, dataarray)
plot.axhline(y=np.mean(dataarray), color='r', linestyle='-')
plot.show()