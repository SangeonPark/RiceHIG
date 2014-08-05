import FWCore.ParameterSet.Config as cms

epetadeco_ana = cms.EDAnalyzer('EPEtaDecoAnalyzer',

  TrgTrackCollection = cms.string('generalTracks'),
  VertexCollection = cms.string('offlinePrimaryVertices'),
  GenParticleCollection = cms.string('genParticles'),
  V0CandidateCollection = cms.string('generalV0CandidatesNew'),

  TriggerID = cms.string('Track'),
  AssociateID = cms.string('CaloTower'),

  NEtaBins = cms.int32(40),
  NPhiBins = cms.int32(36),
  checksign = cms.int32(-1),

  nmin = cms.int32(-1),
  nmax = cms.int32(-1),
  centmin = cms.int32(-1),
  centmax = cms.int32(-1),
  zvtxmin = cms.double(-150),
  zvtxmax = cms.double(150),
  zvtxbin = cms.double(300),
  rhomin = cms.double(0.0),
  rhomax = cms.double(0.2),
  xvtxcenter = cms.double(0.077),
  yvtxcenter = cms.double(0.037),
  zvtxcenter = cms.double(-0.54),
  etatrgmin = cms.double(-2.4),
  etatrgmax = cms.double(2.4),
  etaassmin = cms.double(4.0),
  etaassmax = cms.double(5.0),
  pttrgmin = cms.vdouble(0.3),
  pttrgmax = cms.vdouble(3.0),
  ptassmin = cms.vdouble(0.0),
  ptassmax = cms.vdouble(10000.0),
  etamultmin = cms.double(-2.4),
  etamultmax = cms.double(2.4),
  ptmultmin = cms.double(0.4),
  ptmultmax = cms.double(10000),
  runmin = cms.int32(-1),
  runmax = cms.int32(-1),

  mass_trg = cms.double(0.140),
  mass_ass = cms.double(0.140),
  genpdgId_trg = cms.int32(-999999),
  genpdgId_ass = cms.int32(-999999),
  isstable_trg = cms.bool(True),
  isstable_ass = cms.bool(True),
  ischarge_trg = cms.bool(True),
  ischarge_ass = cms.bool(True),

  IsGenMult = cms.bool(False),
  IsVtxSel = cms.bool(True),
  IsCorr = cms.bool(True),
  IsHI = cms.bool(True),
  IsFullMatrix = cms.bool(True),
  IsPtWeightTrg = cms.bool(False),
  IsPtWeightAss = cms.bool(True),
  IsHITrkQuality = cms.bool(False),
  IsPPTrkQuality = cms.bool(True),
  IsDebug = cms.bool(False),
  IsInvMass = cms.bool(False),
  IsEventEngineer = cms.bool(False)
)
