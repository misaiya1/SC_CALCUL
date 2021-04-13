# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class SC_CALCUL
###########################################################################

class SC_CALCUL ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"鼠笼风电机组电驱系统设计工具", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"输入参数", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText15.Wrap( -1 )
		
		self.m_staticText15.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer5.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		fgSizer3 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_Tpp = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"极对数", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Tpp.Wrap( -1 )
		
		fgSizer3.Add( self.m_Tpp, 0, wx.ALL, 5 )
		
		self.m_pp = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_pp, 0, wx.ALL, 5 )
		
		self.m_Tpp1 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"发电机额定功率[kW]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Tpp1.Wrap( -1 )
		
		fgSizer3.Add( self.m_Tpp1, 0, wx.ALL, 5 )
		
		self.m_GenPower = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"4250", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_GenPower, 0, wx.ALL, 5 )
		
		self.m_Thz = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"电网频率[Hz]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Thz.Wrap( -1 )
		
		fgSizer3.Add( self.m_Thz, 0, wx.ALL, 5 )
		
		self.m_hz = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_hz, 0, wx.ALL, 5 )
		
		self.m_Thz1 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"额定频率[Hz]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Thz1.Wrap( -1 )
		
		fgSizer3.Add( self.m_Thz1, 0, wx.ALL, 5 )
		
		self.m_edhz = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"48.9", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_edhz, 0, wx.ALL, 5 )
		
		self.m_staticText212 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"变流器效率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		
		fgSizer3.Add( self.m_staticText212, 0, wx.ALL, 5 )
		
		self.m_XiaoLv = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"0.97", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_XiaoLv, 0, wx.ALL, 5 )
		
		self.m_staticText2121 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"电机效率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2121.Wrap( -1 )
		
		fgSizer3.Add( self.m_staticText2121, 0, wx.ALL, 5 )
		
		self.m_XiaoLvGen = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"0.97", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_XiaoLvGen, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"发电机额定电压[V]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		
		fgSizer3.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_RateVolt = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"750", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_RateVolt, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"电网电压[V]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		
		fgSizer3.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_GridVRMS = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"690", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_GridVRMS, 0, wx.ALL, 5 )
		
		self.m_Vdc2111 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)发电机额定电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Vdc2111.Wrap( -1 )
		
		fgSizer3.Add( self.m_Vdc2111, 0, wx.ALL, 5 )
		
		self.m_RateGenCurrent = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"3895", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_RateGenCurrent, 0, wx.ALL, 5 )
		
		self.m_Vdc211 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)额定直流母线电压[V]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Vdc211.Wrap( -1 )
		
		fgSizer3.Add( self.m_Vdc211, 0, wx.ALL, 5 )
		
		self.m_Vdc = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1120", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_Vdc, 0, wx.ALL, 5 )
		
		self.m_SetNetMaxI11 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)网侧变流器额定电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetNetMaxI11.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetNetMaxI11, 0, wx.ALL, 5 )
		
		self.m_SetNetCurRate = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"3456", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetNetCurRate, 0, wx.ALL, 5 )
		
		self.m_SetNetMaxI1 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)网侧变流器极限电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetNetMaxI1.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetNetMaxI1, 0, wx.ALL, 5 )
		
		self.m_SetNetCurMax = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"4446", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetNetCurMax, 0, wx.ALL, 5 )
		
		self.m_SetGenMaxI111 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)机侧变流器额定电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetGenMaxI111.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetGenMaxI111, 0, wx.ALL, 5 )
		
		self.m_SetGenCurRate = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"3815", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetGenCurRate, 0, wx.ALL, 5 )
		
		self.m_SetGenMaxI11 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)机侧变流器极限电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetGenMaxI11.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetGenMaxI11, 0, wx.ALL, 5 )
		
		self.m_SetGenCurMax = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"4440", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetGenCurMax, 0, wx.ALL, 5 )
		
		self.m_SetSatMaxI1111 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)发电机定子极限电流[A]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SetSatMaxI1111.Wrap( -1 )
		
		fgSizer3.Add( self.m_SetSatMaxI1111, 0, wx.ALL, 5 )
		
		self.m_SetSatMaxI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"1503", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_SetSatMaxI, 0, wx.ALL, 5 )
		
		self.m_Tgonet = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"(选填)备用", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Tgonet.Wrap( -1 )
		
		fgSizer3.Add( self.m_Tgonet, 0, wx.ALL, 5 )
		
		self.m_GoNetPower = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_GoNetPower, 0, wx.ALL, 5 )
		
		
		self.m_scrolledWindow2.SetSizer( fgSizer3 )
		self.m_scrolledWindow2.Layout()
		fgSizer3.Fit( self.m_scrolledWindow2 )
		bSizer51.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"输入激磁电抗、定子漏抗、转子漏抗折算", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		fgSizer31 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText221 = wx.StaticText( self, wx.ID_ANY, u"定子电组[ohm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )
		
		bSizer13.Add( self.m_staticText221, 0, wx.ALL, 5 )
		
		self.m_Rs = wx.TextCtrl( self, wx.ID_ANY, u"6.67E-4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_Rs, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2211 = wx.StaticText( self, wx.ID_ANY, u"转子电阻[ohm]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2211.Wrap( -1 )
		
		bSizer131.Add( self.m_staticText2211, 0, wx.ALL, 5 )
		
		self.m_Rr = wx.TextCtrl( self, wx.ID_ANY, u"6.33E-4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_Rr, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer131, 1, wx.EXPAND, 5 )
		
		bSizer132 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_Lksss = wx.StaticText( self, wx.ID_ANY, u"定子漏感[H]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Lksss.Wrap( -1 )
		
		bSizer132.Add( self.m_Lksss, 0, wx.ALL, 5 )
		
		self.m_Lks = wx.TextCtrl( self, wx.ID_ANY, u"4.67E-5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer132.Add( self.m_Lks, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer132, 1, wx.EXPAND, 5 )
		
		bSizer133 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_Lkrrr = wx.StaticText( self, wx.ID_ANY, u"转子漏感[H]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_Lkrrr.Wrap( -1 )
		
		bSizer133.Add( self.m_Lkrrr, 0, wx.ALL, 5 )
		
		self.m_Lkr = wx.TextCtrl( self, wx.ID_ANY, u"3.47E-5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer133.Add( self.m_Lkr, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer133, 1, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"电机互感[H]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		
		bSizer101.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_Lm = wx.TextCtrl( self, wx.ID_ANY, u"1.01E-3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer101.Add( self.m_Lm, 0, wx.ALL, 5 )
		
		
		fgSizer31.Add( bSizer101, 1, wx.EXPAND, 5 )
		
		
		bSizer51.Add( fgSizer31, 0, 0, 5 )
		
		self.m_staticText1711 = wx.StaticText( self, wx.ID_ANY, u"转矩曲线表", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1711.Wrap( -1 )
		
		bSizer51.Add( self.m_staticText1711, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid2.CreateGrid( 4, 26 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 20 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer51.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"磁链给定说明：弱磁区间，手动给定，低速阶段根据空载开路电压计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		
		bSizer51.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		gSizer5 = wx.GridSizer( 1, 3, 0, 0 )
		
		bSizer134 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrlS = wx.TextCtrl( self, wx.ID_ANY, u"550", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer134.Add( self.m_textCtrlS, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText171 = wx.StaticText( self, wx.ID_ANY, u"右侧计算使用的转速点[RPM]", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText171.Wrap( -1 )
		
		bSizer134.Add( self.m_staticText171, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		gSizer5.Add( bSizer134, 1, wx.EXPAND, 5 )
		
		self.m_button = wx.Button( self, wx.ID_ANY, u"重新单点计算", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"报告生成", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer51.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"计算结果(转速点)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText16.Wrap( -1 )
		
		self.m_staticText16.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer7.Add( self.m_staticText16, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticTextV = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"V:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextV.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextV, 0, wx.ALL, 5 )
		
		self.m_V = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_V, 0, wx.ALL, 5 )
		
		self.m_staticTextW = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"W:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextW.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextW, 0, wx.ALL, 5 )
		
		self.m_W = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_W, 0, wx.ALL, 5 )
		
		self.m_staticTextQ = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Q:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextQ.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextQ, 0, wx.ALL, 5 )
		
		self.m_Q = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_Q, 0, wx.ALL, 5 )
		
		self.m_staticTextR = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"R:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextR.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextR, 0, wx.ALL, 5 )
		
		self.m_R = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_R, 0, wx.ALL, 5 )
		
		self.m_staticTextX = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"X:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextX.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextX, 0, wx.ALL, 5 )
		
		self.m_X = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_X, 0, wx.ALL, 5 )
		
		self.m_staticTextZ = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Z:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextZ.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextZ, 0, wx.ALL, 5 )
		
		self.m_Z = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_Z, 0, wx.ALL, 5 )
		
		self.m_staticTextAB = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AB:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAB.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAB, 0, wx.ALL, 5 )
		
		self.m_AB = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AB, 0, wx.ALL, 5 )
		
		self.m_staticTextAD = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAD.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAD, 0, wx.ALL, 5 )
		
		self.m_AD = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AD, 0, wx.ALL, 5 )
		
		self.m_staticTextAF = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAF.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAF, 0, wx.ALL, 5 )
		
		self.m_AF = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AF, 0, wx.ALL, 5 )
		
		self.m_staticTextAH = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AH:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAH.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAH, 0, wx.ALL, 5 )
		
		self.m_AH = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AH, 0, wx.ALL, 5 )
		
		self.m_staticTextAJ = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AJ:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAJ.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAJ, 0, wx.ALL, 5 )
		
		self.m_AJ = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AJ, 0, wx.ALL, 5 )
		
		self.m_staticTextAK = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AK:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAK.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAK, 0, wx.ALL, 5 )
		
		self.m_AK = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AK, 0, wx.ALL, 5 )
		
		self.m_staticTextAL = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAL.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAL, 0, wx.ALL, 5 )
		
		self.m_AL = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AL, 0, wx.ALL, 5 )
		
		self.m_staticTextAM = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AM:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAM.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAM, 0, wx.ALL, 5 )
		
		self.m_AM = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AM, 0, wx.ALL, 5 )
		
		self.m_staticText441 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText441, 0, wx.ALL, 5 )
		
		self.m_staticText442 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText442.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText442, 0, wx.ALL, 5 )
		
		self.m_staticTextT = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"T:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextT.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextT, 0, wx.ALL, 5 )
		
		self.m_T = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_T, 0, wx.ALL, 5 )
		
		self.m_staticTextU = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"U:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextU.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextU, 0, wx.ALL, 5 )
		
		self.m_U = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_U, 0, wx.ALL, 5 )
		
		self.m_staticTextY = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Y:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextY.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextY, 0, wx.ALL, 5 )
		
		self.m_Y = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_Y, 0, wx.ALL, 5 )
		
		self.m_staticTextAA = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AA:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAA.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAA, 0, wx.ALL, 5 )
		
		self.m_AA = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AA, 0, wx.ALL, 5 )
		
		self.m_staticTextAC = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAC.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAC, 0, wx.ALL, 5 )
		
		self.m_AC = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AC, 0, wx.ALL, 5 )
		
		self.m_staticTextAE = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AE:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAE.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAE, 0, wx.ALL, 5 )
		
		self.m_AE = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AE, 0, wx.ALL, 5 )
		
		self.m_staticTextAG = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AG:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAG.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAG, 0, wx.ALL, 5 )
		
		self.m_AG = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AG, 0, wx.ALL, 5 )
		
		self.m_staticTextAI = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AI:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAI.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAI, 0, wx.ALL, 5 )
		
		self.m_AI = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AI, 0, wx.ALL, 5 )
		
		self.m_staticTextAN = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AN:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAN.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAN, 0, wx.ALL, 5 )
		
		self.m_AN = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AN, 0, wx.ALL, 5 )
		
		self.m_staticTextAO = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AO:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAO.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAO, 0, wx.ALL, 5 )
		
		self.m_AO = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AO, 0, wx.ALL, 5 )
		
		self.m_staticTextAP = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAP.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAP, 0, wx.ALL, 5 )
		
		self.m_AP = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AP, 0, wx.ALL, 5 )
		
		self.m_staticTextAQ = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AQ:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAQ.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAQ, 0, wx.ALL, 5 )
		
		self.m_AQ = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AQ, 0, wx.ALL, 5 )
		
		self.m_staticText4412 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4412.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText4412, 0, wx.ALL, 5 )
		
		self.m_staticText4411 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4411.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticText4411, 0, wx.ALL, 5 )
		
		self.m_staticTextAS = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AS:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAS.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAS, 0, wx.ALL, 5 )
		
		self.m_AS = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AS, 0, wx.ALL, 5 )
		
		self.m_staticTextAT = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAT.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAT, 0, wx.ALL, 5 )
		
		self.m_AT = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AT, 0, wx.ALL, 5 )
		
		self.m_staticTextAU = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AU:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAU.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAU, 0, wx.ALL, 5 )
		
		self.m_AU = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AU, 0, wx.ALL, 5 )
		
		self.m_staticTextAV = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AV:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAV.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAV, 0, wx.ALL, 5 )
		
		self.m_AV = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AV, 0, wx.ALL, 5 )
		
		self.m_staticTextAW = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AW:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAW.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAW, 0, wx.ALL, 5 )
		
		self.m_AW = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AW, 0, wx.ALL, 5 )
		
		self.m_staticTextAX = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AX:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAX.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAX, 0, wx.ALL, 5 )
		
		self.m_AX = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AX, 0, wx.ALL, 5 )
		
		self.m_staticTextAY = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"AY:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextAY.Wrap( -1 )
		
		fgSizer4.Add( self.m_staticTextAY, 0, wx.ALL, 5 )
		
		self.m_AY = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_AY, 0, wx.ALL, 5 )
		
		
		bSizer71.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer71 )
		self.m_scrolledWindow1.Layout()
		bSizer71.Fit( self.m_scrolledWindow1 )
		bSizer7.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		gSizer3.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"说明信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"版本信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu5, u"说明" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.OnCheck )
		self.m_button.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick )
		self.m_button2.Bind( wx.EVT_BUTTON, self.m_buttonOnButtonClick2 )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection2, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection1, id = self.m_menuItem3.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCheck( self, event ):
		event.Skip()
	
	def m_buttonOnButtonClick( self, event ):
		event.Skip()
	
	def m_buttonOnButtonClick2( self, event ):
		event.Skip()
	
	def mOnMenuSelection2( self, event ):
		event.Skip()
	
	def mOnMenuSelection1( self, event ):
		event.Skip()
	

