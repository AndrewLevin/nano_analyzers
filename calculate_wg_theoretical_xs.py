import ROOT
import math

from math import hypot, pi
def deltaR(eta1,phi1,eta2,phi2):
    dphi = abs(phi1-phi2);
    if dphi > pi: dphi = 2*pi-dphi
    return hypot(eta1-eta2,dphi)

#f=ROOT.TFile.Open("/afs/cern.ch/work/a/amlevin/tmp/BD10FEDE-2447-174B-8426-4BE7869483C4.root") #powheg plus
#f=ROOT.TFile.Open("/afs/cern.ch/work/a/amlevin/tmp/2DCB7126-1603-8D4C-BF2C-51991D71D4F8.root") #powheg minus
#f=ROOT.TFile.Open("/afs/cern.ch/work/a/amlevin/tmp/EFC1BDD3-7856-3B4B-9BBE-1A35E0041590.root") #mg5_aMC
f=ROOT.TFile.Open("/afs/cern.ch/work/a/amlevin/tmp/wgjets.root") #mg5_aMC
t=f.Get("Events")

sample_xs = 178.6
#sample_xs = 33420.0 
#sample_xs = 24780.0

n_total = 0
n_weighted = ROOT.TH1F("n_weighted","n_weighted",1,0,1)
n_weighted.Sumw2()
n_weighted_pass_fiducial = ROOT.TH1F("n_weighted_pass_fiducial","n_weighted_fiducial",1,0,1)
n_weighted_pass_fiducial.Sumw2()
n_weighted_pdf = []
n_weighted_scale = []
n_weighted_pdf_pass_fiducial = []
n_weighted_scale_pass_fiducial = []

n_total_plus = 0
n_weighted_plus = ROOT.TH1F("n_weighted_plus","n_weighted_plus",1,0,1)
n_weighted_plus.Sumw2()
n_weighted_pass_fiducial_plus = ROOT.TH1F("n_weighted_pass_fiducial_plus","n_weighted_fiducial_plus",1,0,1)
n_weighted_pass_fiducial_plus.Sumw2()
n_weighted_pdf_plus = []
n_weighted_scale_plus = []
n_weighted_pdf_pass_fiducial_plus = []
n_weighted_scale_pass_fiducial_plus = []

n_total_minus = 0
n_weighted_minus = ROOT.TH1F("n_weighted_minus","n_weighted_minus",1,0,1)
n_weighted_minus.Sumw2()
n_weighted_pass_fiducial_minus = ROOT.TH1F("n_weighted_pass_fiducial_minus","n_weighted_fiducial_minus",1,0,1)
n_weighted_pass_fiducial_minus.Sumw2()
n_weighted_pdf_minus = []
n_weighted_scale_minus = []
n_weighted_pdf_pass_fiducial_minus = []
n_weighted_scale_pass_fiducial_minus = []

for i in range(0,32):
    n_weighted_pdf.append(ROOT.TH1F("n_weighted_pdf_variation"+str(i),"n_weighted_pdf_variation"+str(i),1,0,1))
    n_weighted_pdf[i].Sumw2()
    n_weighted_pdf_pass_fiducial.append(ROOT.TH1F("n_weighted_pass_fiducial_pdf_variation"+str(i),"n_weighted_pass_fiducial_pdf_variation"+str(i),1,0,1))
    n_weighted_pdf_pass_fiducial[i].Sumw2()

    n_weighted_pdf_plus.append(ROOT.TH1F("n_weighted_plus_pdf_variation"+str(i),"n_weighted_plus_pdf_variation"+str(i),1,0,1))
    n_weighted_pdf_plus[i].Sumw2()
    n_weighted_pdf_pass_fiducial_plus.append(ROOT.TH1F("n_weighted_pass_fiducial_plus_pdf_variation"+str(i),"n_weighted_pass_fiducial_plus_pdf_variation"+str(i),1,0,1))
    n_weighted_pdf_pass_fiducial_plus[i].Sumw2()

    n_weighted_pdf_minus.append(ROOT.TH1F("n_weighted_minus_pdf_variation"+str(i),"n_weighted_minus_pdf_variation"+str(i),1,0,1))
    n_weighted_pdf_minus[i].Sumw2()
    n_weighted_pdf_pass_fiducial_minus.append(ROOT.TH1F("n_weighted_pass_fiducial_minus_pdf_variation"+str(i),"n_weighted_pass_fiducial_minus_pdf_variation"+str(i),1,0,1))
    n_weighted_pdf_pass_fiducial_minus[i].Sumw2()

for i in range(0,8):
    n_weighted_scale.append(ROOT.TH1F("n_weighted_scale_variation"+str(i),"n_weighted_scale_variation"+str(i),1,0,1))
    n_weighted_scale[i].Sumw2()
    n_weighted_scale_pass_fiducial.append(ROOT.TH1F("n_weighted_pass_fiducial_scale_variation"+str(i),"n_weighted_pass_fiducial_scale_variation"+str(i),1,0,1))
    n_weighted_scale_pass_fiducial[i].Sumw2()

    n_weighted_scale_plus.append(ROOT.TH1F("n_weighted_plus_scale_variation"+str(i),"n_weighted_plus_scale_variation"+str(i),1,0,1))
    n_weighted_scale_plus[i].Sumw2()
    n_weighted_scale_pass_fiducial_plus.append(ROOT.TH1F("n_weighted_pass_fiducial_plus_scale_variation"+str(i),"n_weighted_pass_fiducial_plus_scale_variation"+str(i),1,0,1))
    n_weighted_scale_pass_fiducial_plus[i].Sumw2()

    n_weighted_scale_minus.append(ROOT.TH1F("n_weighted_minus_scale_variation"+str(i),"n_weighted_minus_scale_variation"+str(i),1,0,1))
    n_weighted_scale_minus[i].Sumw2()
    n_weighted_scale_pass_fiducial_minus.append(ROOT.TH1F("n_weighted_pass_fiducial_minus_scale_variation"+str(i),"n_weighted_pass_fiducial_minus_scale_variation"+str(i),1,0,1))
    n_weighted_scale_pass_fiducial_minus[i].Sumw2()

isprompt_mask = (1 << 0) #isPrompt                                                                                                                           
isfromhardprocess_mask = (1 << 8) #isFromHardProcess                                                                                                         
isdirectprompttaudecayproduct_mask = (1 << 5) #isDirectPromptTauDecayProduct

print "t.GetEntries() = "+str(t.GetEntries())
for i in range(0,t.GetEntries()):
    if n_total % 10000 == 0:
        print "n_total = "+str(n_total)
    n_total+=1
    t.GetEntry(i)
    n_gen_leptons = 0
    n_gen_photons = 0

    for j in range(0,t.nGenPart):
        if t.GenPart_pt[j] > 25 and t.GenPart_status[j] == 1 and (abs(t.GenPart_pdgId[j]) == 11 or abs(t.GenPart_pdgId[j]) == 13):
            lep_iso=0
            for k in range(0,t.nGenPart):

                if k == j:
                    continue
                        
                if  t.GenPart_status[k] != 1:
                    continue

                if abs(t.GenPart_pdgId[k]) == 12 or abs(t.GenPart_pdgId[k]) == 14 or abs(t.GenPart_pdgId[k]) == 16:
                    continue

                if deltaR(t.GenPart_eta[k],t.GenPart_phi[k],t.GenPart_eta[j],t.GenPart_phi[j]) < 0.4:
                    lep_iso += t.GenPart_pt[k]

                lep_iso /= t.GenPart_pt[j]

                if lep_iso < 0.5:
                    if n_gen_leptons == 0:
                        gen_lepton_index = j
                    n_gen_leptons +=1

        if t.GenPart_pt[j] > 25 and t.GenPart_status[j] == 1 and t.GenPart_pdgId[j] == 22 and abs(t.GenPart_eta[j]) < 2.5:
            pho_iso=0
            for k in range(0,t.nGenPart):

                if k == j:
                    continue
                        
                if  t.GenPart_status[k] != 1:
                    continue

                if abs(t.GenPart_pdgId[k]) == 12 or abs(t.GenPart_pdgId[k]) == 14 or abs(t.GenPart_pdgId[k]) == 16:
                    continue

                if deltaR(t.GenPart_eta[k],t.GenPart_phi[k],t.GenPart_eta[j],t.GenPart_phi[j]) < 0.4:
                    pho_iso += t.GenPart_pt[k]

                pho_iso /= t.GenPart_pt[j]

                if pho_iso < 0.5:
                    if n_gen_photons == 0:
                        gen_photon_index = j
                    n_gen_photons +=1

    pass_fiducial = False

    if n_gen_leptons >= 1 and n_gen_photons >= 1:
        if deltaR(t.GenPart_eta[gen_lepton_index],t.GenPart_phi[gen_lepton_index],t.GenPart_eta[gen_photon_index],t.GenPart_phi[gen_photon_index]) > 0.5 and t.GenPart_pt[gen_lepton_index] > 25 and t.GenPart_pt[gen_photon_index] > 25 and abs(t.GenPart_eta[gen_lepton_index]) < 2.5 and abs(t.GenPart_eta[gen_photon_index]) < 2.5 and t.GenMET_pt > 40:
            pass_fiducial = True

#    assert(n_gen_leptons == 1 or n_gen_leptons == 0)
#    assert(n_gen_photons == 1 or n_gen_photons == 0)

    if t.Generator_weight > 0:
        n_weighted.Fill(0.5)
    else:    
        n_weighted.Fill(0.5,-1)

    for j in range(0,8):
        if t.Generator_weight > 0:
            n_weighted_scale[j].Fill(0.5,t.LHEScaleWeight[j]*2)
        else:    
            n_weighted_scale[j].Fill(0.5,-t.LHEScaleWeight[j]*2)
    for j in range(0,32):
        if t.Generator_weight > 0:
            n_weighted_pdf[j].Fill(0.5,t.LHEPdfWeight[j+1])
        else:    
            n_weighted_pdf[j].Fill(0.5,-t.LHEPdfWeight[j+1])

    if pass_fiducial:        
        if t.Generator_weight > 0:
            n_weighted_pass_fiducial.Fill(0.5)
            if t.GenPart_pdgId[gen_lepton_index] < 0:
                n_weighted_pass_fiducial_plus.Fill(0.5)
            else:    
                n_weighted_pass_fiducial_minus.Fill(0.5)
        else:    
            n_weighted_pass_fiducial.Fill(0.5,-1)
            if t.GenPart_pdgId[gen_lepton_index] < 0:
                n_weighted_pass_fiducial_plus.Fill(0.5,-1)
            else:    
                n_weighted_pass_fiducial_minus.Fill(0.5,-1)

        for j in range(0,8):
            if t.Generator_weight > 0:
                n_weighted_scale_pass_fiducial[j].Fill(0.5,t.LHEScaleWeight[j]*2)
                if t.GenPart_pdgId[gen_lepton_index] < 0:
                    n_weighted_scale_pass_fiducial_plus[j].Fill(0.5,t.LHEScaleWeight[j]*2)
                else:    
                    n_weighted_scale_pass_fiducial_minus[j].Fill(0.5,t.LHEScaleWeight[j]*2)
            else:    
                n_weighted_scale_pass_fiducial[j].Fill(0.5,-t.LHEScaleWeight[j]*2)
                if t.GenPart_pdgId[gen_lepton_index] < 0:
                    n_weighted_scale_pass_fiducial_plus[j].Fill(0.5,-t.LHEScaleWeight[j]*2)
                else:    
                    n_weighted_scale_pass_fiducial_minus[j].Fill(0.5,-t.LHEScaleWeight[j]*2)
        for j in range(0,32):
            if t.Generator_weight > 0:
                n_weighted_pdf_pass_fiducial[j].Fill(0.5,t.LHEPdfWeight[j+1])
                if t.GenPart_pdgId[gen_lepton_index] < 0:
                    n_weighted_pdf_pass_fiducial_plus[j].Fill(0.5,t.LHEPdfWeight[j+1])
                else:    
                    n_weighted_pdf_pass_fiducial_minus[j].Fill(0.5,t.LHEPdfWeight[j+1])
            else:    
                n_weighted_pdf_pass_fiducial[j].Fill(0.5,-t.LHEPdfWeight[j+1])
                if t.GenPart_pdgId[gen_lepton_index] < 0:
                    n_weighted_pdf_pass_fiducial_plus[j].Fill(0.5,-t.LHEPdfWeight[j+1])
                else:    
                    n_weighted_pdf_pass_fiducial_minus[j].Fill(0.5,-t.LHEPdfWeight[j+1])


print "fiducial_region_cuts_efficiency = " + str(n_weighted_pass_fiducial.GetBinContent(1)/n_weighted.GetBinContent(1))
print "fiducial_region_cuts_efficiency_plus = " + str(n_weighted_pass_fiducial_plus.GetBinContent(1)/n_weighted.GetBinContent(1))
print "fiducial_region_cuts_efficiency_minus = " + str(n_weighted_pass_fiducial_minus.GetBinContent(1)/n_weighted.GetBinContent(1))

print "n_weighted.GetBinContent(1) = "+str(n_weighted.GetBinContent(1))
print "n_weighted.GetBinError(1) = " + str(n_weighted.GetBinError(1))

print "n_weighted_plus.GetBinContent(1) = "+str(n_weighted_plus.GetBinContent(1))
print "n_weighted_minus.GetBinError(1) = " + str(n_weighted_minus.GetBinError(1))

pdf_mean = 0
pdf_stddev = 0
scale_mean = 0
scale_stddev = 0

pdf_pass_fiducial_mean = 0
pdf_pass_fiducial_stddev = 0
scale_pass_fiducial_mean = 0
scale_pass_fiducial_stddev = 0

pdf_mean_plus = 0
pdf_stddev_plus = 0
scale_mean_plus = 0
scale_stddev_plus = 0

pdf_pass_fiducial_mean_plus = 0
pdf_pass_fiducial_stddev_plus = 0
scale_pass_fiducial_mean_plus = 0
scale_pass_fiducial_stddev_plus = 0

pdf_mean_minus = 0
pdf_stddev_minus = 0
scale_mean_minus = 0
scale_stddev_minus = 0

pdf_pass_fiducial_mean_minus = 0
pdf_pass_fiducial_stddev_minus = 0
scale_pass_fiducial_mean_minus = 0
scale_pass_fiducial_stddev_minus = 0

for i in range(0,32):
    pdf_mean+=n_weighted_pdf[i].GetBinContent(1)
    pdf_pass_fiducial_mean+=n_weighted_pdf_pass_fiducial[i].GetBinContent(1)

    pdf_mean_plus+=n_weighted_pdf_plus[i].GetBinContent(1)
    pdf_pass_fiducial_mean_plus+=n_weighted_pdf_pass_fiducial_plus[i].GetBinContent(1)

    pdf_mean_minus+=n_weighted_pdf_minus[i].GetBinContent(1)
    pdf_pass_fiducial_mean_minus+=n_weighted_pdf_pass_fiducial_minus[i].GetBinContent(1)

pdf_mean += n_weighted.GetBinContent(1)
pdf_pass_fiducial_mean += n_weighted_pass_fiducial.GetBinContent(1)

pdf_mean_plus += n_weighted_plus.GetBinContent(1)
pdf_pass_fiducial_mean_plus += n_weighted_pass_fiducial_plus.GetBinContent(1)

pdf_mean_minus += n_weighted_minus.GetBinContent(1)
pdf_pass_fiducial_mean_minus += n_weighted_pass_fiducial_minus.GetBinContent(1)

pdf_mean /= 33
pdf_pass_fiducial_mean /= 33

pdf_mean_plus /= 33
pdf_pass_fiducial_mean_plus /= 33

pdf_mean_minus /= 33
pdf_pass_fiducial_mean_minus /= 33

for i in range(0,32):
    pdf_stddev+= pow(n_weighted_pdf[i].GetBinContent(1)-pdf_mean,2)
    pdf_pass_fiducial_stddev+= pow(n_weighted_pdf_pass_fiducial[i].GetBinContent(1)-pdf_pass_fiducial_mean,2)

    pdf_stddev_plus+= pow(n_weighted_pdf_plus[i].GetBinContent(1)-pdf_mean_plus,2)
    pdf_pass_fiducial_stddev_plus+= pow(n_weighted_pdf_pass_fiducial_plus[i].GetBinContent(1)-pdf_pass_fiducial_mean_plus,2)

    pdf_stddev_minus+= pow(n_weighted_pdf_minus[i].GetBinContent(1)-pdf_mean_minus,2)
    pdf_pass_fiducial_stddev_minus+= pow(n_weighted_pdf_pass_fiducial_minus[i].GetBinContent(1)-pdf_pass_fiducial_mean_minus,2)

pdf_stddev += pow(n_weighted.GetBinContent(1)-pdf_mean,2)
pdf_pass_fiducial_stddev += pow(n_weighted_pass_fiducial.GetBinContent(1)-pdf_pass_fiducial_mean,2)

pdf_stddev_plus += pow(n_weighted_plus.GetBinContent(1)-pdf_mean_plus,2)
pdf_pass_fiducial_stddev_plus += pow(n_weighted_pass_fiducial_plus.GetBinContent(1)-pdf_pass_fiducial_mean_plus,2)

pdf_stddev_minus += pow(n_weighted_minus.GetBinContent(1)-pdf_mean_minus,2)
pdf_pass_fiducial_stddev_minus += pow(n_weighted_pass_fiducial_minus.GetBinContent(1)-pdf_pass_fiducial_mean_minus,2)

pdf_stddev /= (33-1)
pdf_pass_fiducial_stddev /= (33-1)

pdf_stddev_plus /= (33-1)
pdf_pass_fiducial_stddev_plus /= (33-1)

pdf_stddev_minus /= (33-1)
pdf_pass_fiducial_stddev_minus /= (33-1)

pdf_stddev = math.sqrt(pdf_stddev)
pdf_pass_fiducial_stddev = math.sqrt(pdf_pass_fiducial_stddev)

pdf_stddev_plus = math.sqrt(pdf_stddev_plus)
pdf_pass_fiducial_stddev_plus = math.sqrt(pdf_pass_fiducial_stddev_plus)

pdf_stddev_minus = math.sqrt(pdf_stddev_minus)
pdf_pass_fiducial_stddev_minus = math.sqrt(pdf_pass_fiducial_stddev_minus)

for i in range(0,8):
    if i == 6 or i == 4:
        continue

    scale_mean += n_weighted_scale[i].GetBinContent(1)
    scale_pass_fiducial_mean += n_weighted_scale_pass_fiducial[i].GetBinContent(1)

    scale_mean_plus += n_weighted_scale_plus[i].GetBinContent(1)
    scale_pass_fiducial_mean_plus += n_weighted_scale_pass_fiducial_plus[i].GetBinContent(1)

    scale_mean_minus += n_weighted_scale_minus[i].GetBinContent(1)
    scale_pass_fiducial_mean_minus += n_weighted_scale_pass_fiducial_minus[i].GetBinContent(1)

scale_mean += n_weighted.GetBinContent(1)
scale_pass_fiducial_mean += n_weighted_pass_fiducial.GetBinContent(1)

scale_mean_plus += n_weighted_plus.GetBinContent(1)
scale_pass_fiducial_mean_plus += n_weighted_pass_fiducial_plus.GetBinContent(1)

scale_mean_minus += n_weighted_minus.GetBinContent(1)
scale_pass_fiducial_mean_minus += n_weighted_pass_fiducial_minus.GetBinContent(1)

scale_mean /= 7
scale_pass_fiducial_mean /= 7

scale_mean_plus /= 7
scale_pass_fiducial_mean_plus /= 7

scale_mean_minus /= 7
scale_pass_fiducial_mean_minus /= 7

for i in range(0,8):
    if i == 6 or i == 4:
        continue

    scale_stddev += pow(n_weighted_scale[i].GetBinContent(1)-scale_mean,2)
    scale_pass_fiducial_stddev += pow(n_weighted_scale_pass_fiducial[i].GetBinContent(1)-scale_pass_fiducial_mean,2)

    scale_stddev_plus += pow(n_weighted_scale_plus[i].GetBinContent(1)-scale_mean_plus,2)
    scale_pass_fiducial_stddev_plus += pow(n_weighted_scale_pass_fiducial_plus[i].GetBinContent(1)-scale_pass_fiducial_mean_plus,2)

    scale_stddev_minus += pow(n_weighted_scale_minus[i].GetBinContent(1)-scale_mean_minus,2)
    scale_pass_fiducial_stddev_minus += pow(n_weighted_scale_pass_fiducial_minus[i].GetBinContent(1)-scale_pass_fiducial_mean_minus,2)

scale_stddev += pow(n_weighted.GetBinContent(1)-scale_mean,2)
scale_pass_fiducial_stddev += pow(n_weighted_pass_fiducial.GetBinContent(1)-scale_pass_fiducial_mean,2)

scale_stddev_plus += pow(n_weighted_plus.GetBinContent(1)-scale_mean_plus,2)
scale_pass_fiducial_stddev_plus += pow(n_weighted_pass_fiducial_plus.GetBinContent(1)-scale_pass_fiducial_mean_plus,2)

scale_stddev_minus += pow(n_weighted_minus.GetBinContent(1)-scale_mean_minus,2)
scale_pass_fiducial_stddev_minus += pow(n_weighted_pass_fiducial_minus.GetBinContent(1)-scale_pass_fiducial_mean_minus,2)

scale_stddev /= (7-1)
scale_pass_fiducial_stddev /= (7-1)

scale_stddev_plus /= (7-1)
scale_pass_fiducial_stddev_plus /= (7-1)

scale_stddev_minus /= (7-1)
scale_pass_fiducial_stddev_minus /= (7-1)

scale_stddev = math.sqrt(scale_stddev)
scale_pass_fiducial_stddev = math.sqrt(scale_pass_fiducial_stddev)

scale_stddev_plus = math.sqrt(scale_stddev_plus)
scale_pass_fiducial_stddev_plus = math.sqrt(scale_pass_fiducial_stddev_plus)

scale_stddev_minus = math.sqrt(scale_stddev_minus)
scale_pass_fiducial_stddev_minus = math.sqrt(scale_pass_fiducial_stddev_minus)

nlo_xs = sample_xs

pass_fiducial_nlo_xs = sample_xs * n_weighted_pass_fiducial.GetBinContent(1) / n_weighted.GetBinContent(1)
pass_fiducial_nlo_xs_plus = sample_xs * n_weighted_pass_fiducial_plus.GetBinContent(1) / n_weighted.GetBinContent(1)
pass_fiducial_nlo_xs_minus = sample_xs * n_weighted_pass_fiducial_minus.GetBinContent(1) / n_weighted.GetBinContent(1)

pdf_unc = pdf_stddev * sample_xs / n_weighted.GetBinContent(1)
pdf_pass_fiducial_unc = pdf_pass_fiducial_stddev * sample_xs / n_weighted.GetBinContent(1)

pdf_pass_fiducial_unc_plus = pdf_pass_fiducial_stddev_plus * sample_xs / n_weighted.GetBinContent(1)

pdf_pass_fiducial_unc_minus = pdf_pass_fiducial_stddev_minus * sample_xs / n_weighted.GetBinContent(1)

scale_unc = scale_stddev * sample_xs / n_weighted.GetBinContent(1)
scale_pass_fiducial_unc = scale_pass_fiducial_stddev * sample_xs / n_weighted.GetBinContent(1)
scale_pass_fiducial_unc_plus = scale_pass_fiducial_stddev_plus * sample_xs / n_weighted.GetBinContent(1)
scale_pass_fiducial_unc_minus = scale_pass_fiducial_stddev_minus * sample_xs / n_weighted.GetBinContent(1)

print "efficiency of fiducal region cuts = " + str(n_weighted_pass_fiducial.GetBinContent(1) / n_weighted.GetBinContent(1))
print "efficiency of fiducal region cuts plus = " + str(n_weighted_pass_fiducial_plus.GetBinContent(1) / n_weighted.GetBinContent(1))
print "efficiency of fiducal region cuts minus = " + str(n_weighted_pass_fiducial_minus.GetBinContent(1) / n_weighted.GetBinContent(1))

print "nlo xs = " + str(nlo_xs) + " +/- " + str(scale_unc) + " (scale) +/- " + str(pdf_unc) + " (pdf)" 

print "pass fiducial nlo xs = " + str(pass_fiducial_nlo_xs) + " +/- " + str(scale_pass_fiducial_unc) + " (scale) +/- " + str(pdf_pass_fiducial_unc) + " (pdf)" 

print "pass fiducial nlo xs plus = " + str(pass_fiducial_nlo_xs_plus) + " +/- " + str(scale_pass_fiducial_unc_plus) + " (scale) +/- " + str(pdf_pass_fiducial_unc_plus) + " (pdf)" 

print "pass fiducial nlo xs minus = " + str(pass_fiducial_nlo_xs_minus) + " +/- " + str(scale_pass_fiducial_unc_minus) + " (scale) +/- " + str(pdf_pass_fiducial_unc_minus) + " (pdf)" 

print "100*scale_pass_fiducial_unc/pass_fiducial_nlo_xs = "+str(100*scale_pass_fiducial_unc/pass_fiducial_nlo_xs)

print "100*pdf_pass_fiducial_unc/pass_fiducial_nlo_xs = "+str(100*pdf_pass_fiducial_unc/pass_fiducial_nlo_xs)
