import pscc2018 as ps
import time

app = ps.Dispatch('Photoshop.Application.120')

psDisplayNoDialogs = 3
for index, x in enumerate(range(50)):
    # app.DoAction('Sepia Toning (layer)', 'Default Actions')

    # Execute an existing action from action palette
    # Got this from Scripting listener log on desktop
    idPly = app.CharIDToTypeID("Ply ")
    desc8 = ps.ActionDescriptor()
    idnull = app.CharIDToTypeID("null")
    ref3 = ps.ActionReference()
    idActn = app.CharIDToTypeID("Actn")
    ref3.PutName(idActn, "Sepia Toning (layer)")
    idASet = app.CharIDToTypeID("ASet")
    ref3.PutName(idASet, "Default Actions")
    desc8.PutReference(idnull, ref3)
    app.ExecuteAction(idPly, desc8, psDisplayNoDialogs)
    time.sleep(0.5)

    # Create solid color fill layer.
    idMk = app.CharIDToTypeID("Mk  ")
    desc21 = ps.ActionDescriptor()
    idNull = app.CharIDToTypeID("null")
    ref12 = ps.ActionReference()
    idContentLayer1 = app.StringIDToTypeID("contentLayer")
    ref12.PutClass(idContentLayer1)
    desc21.PutReference(idNull, ref12)
    idUsng = app.CharIDToTypeID("Usng")
    desc22 = ps.ActionDescriptor()
    idType = app.CharIDToTypeID("Type")
    desc23 = ps.ActionDescriptor()
    idClr = app.CharIDToTypeID("Clr ")
    desc24 = ps.ActionDescriptor()
    idRd = app.CharIDToTypeID("Rd  ")
    desc24.PutDouble(idRd, index)
    idGrn = app.CharIDToTypeID("Grn ")
    desc24.PutDouble(idGrn, index)
    idBl = app.CharIDToTypeID("Bl  ")
    desc24.PutDouble(idBl, index)
    idRGBC = app.CharIDToTypeID("RGBC")
    desc23.PutObject(idClr, idRGBC, desc24)
    idSolidColorLayer = app.StringIDToTypeID("solidColorLayer")
    desc22.PutObject(idType, idSolidColorLayer, desc23)
    idContentLayer2 = app.StringIDToTypeID("contentLayer")
    desc21.PutObject(idUsng, idContentLayer2, desc22)
    app.ExecuteAction(idMk, desc21, psDisplayNoDialogs)
    time.sleep(0.5)

    # Select mask
    idSlct = app.CharIDToTypeID("slct")
    desc38 = ps.ActionDescriptor()
    idNull1 = app.CharIDToTypeID("null")
    ref20 = ps.ActionReference()
    idChnl1 = app.CharIDToTypeID("Chnl")
    idChnl2 = app.CharIDToTypeID("Chnl")
    idMsk = app.CharIDToTypeID("Msk ")
    ref20.PutEnumerated(idChnl1, idChnl2, idMsk)
    desc38.PutReference(idNull1, ref20)
    idMkVs = app.CharIDToTypeID("MkVs")
    desc38.PutBoolean(idMkVs, False)
    app.ExecuteAction(idSlct, desc38, psDisplayNoDialogs)
    time.sleep(0.5)

    app.ActiveDocument.ActiveLayer.Invert()

    # doc = app.ActiveDocument


