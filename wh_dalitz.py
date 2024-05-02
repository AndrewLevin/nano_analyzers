import ROOT
import math

from math import hypot, pi
def deltaR(eta1,phi1,eta2,phi2):
    dphi = abs(phi1-phi2);
    if dphi > pi: dphi = 2*pi-dphi
    return hypot(eta1-eta2,dphi)

f=ROOT.TFile.Open("/eos/user/a/amlevin/tmp/Merged.root") 
t=f.Get("Events")

sample_xs = 0.0001147

n_total=0
n_pass=0

isprompt_mask = (1 << 0) #isPrompt                                                                                                                           
isfromhardprocess_mask = (1 << 8) #isFromHardProcess                                                                                                         
isdirectprompttaudecayproduct_mask = (1 << 5) #isDirectPromptTauDecayProduct

print("t.GetEntries() = "+str(t.GetEntries()))
for i in range(0,t.GetEntries()):
    if n_total % 10000 == 0:
        print("n_total = "+str(n_total))
    n_total+=1
    t.GetEntry(i)
    n_gen_leptons = 0
    n_gen_photons = 0

    pass_selection = False                

    for j in range(0,t.nElectron):
        for k in range(0,t.nElectron):
            for l in range(0,t.nMuon):
                for m in range(0,t.nPhoton):
                    if k <= j:
                        continue


                    if t.Muon_pfRelIso04_all[l] > 0.15  or not t.Muon_tightId[l] or t.Muon_pt[l] < 20 or abs(t.Muon_eta[l]) > 2.4:
                        continue

                    if t.Electron_cutBased[j] < 3 or t.Electron_pt[j] < 30 or abs(t.Electron_eta[j]) > 2.5 or t.Electron_cutBased[k] < 3 or t.Electron_pt[k] < 30 or abs(t.Electron_eta[k]) > 2.5:
                        continue

                    if t.Photon_cutBased[m] < 3 or t.Photon_pt[m] < 30 or abs(t.Photon_eta[m]) > 2.5:
                        continue

                    pass_selection = True    

    if pass_selection:
        n_pass = n_pass+1


print(n_pass)

print(sample_xs*138*1000*n_pass/n_total)
