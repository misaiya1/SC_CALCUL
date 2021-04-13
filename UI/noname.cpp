///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jul 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

SC_CALCUL::SC_CALCUL( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxGridSizer* gSizer3;
	gSizer3 = new wxGridSizer( 0, 2, 0, 0 );
	
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText15 = new wxStaticText( this, wxID_ANY, wxT("输入参数"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText15->Wrap( -1 );
	m_staticText15->SetFont( wxFont( 18, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("宋体") ) );
	
	bSizer5->Add( m_staticText15, 0, wxALL|wxEXPAND, 5 );
	
	wxBoxSizer* bSizer51;
	bSizer51 = new wxBoxSizer( wxVERTICAL );
	
	m_scrolledWindow2 = new wxScrolledWindow( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow2->SetScrollRate( 5, 5 );
	wxFlexGridSizer* fgSizer3;
	fgSizer3 = new wxFlexGridSizer( 0, 4, 0, 0 );
	fgSizer3->SetFlexibleDirection( wxBOTH );
	fgSizer3->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_Tpp = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("极对数"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Tpp->Wrap( -1 );
	fgSizer3->Add( m_Tpp, 0, wxALL, 5 );
	
	m_pp = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("2"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_pp, 0, wxALL, 5 );
	
	m_Tpp1 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("发电机额定功率[kW]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Tpp1->Wrap( -1 );
	fgSizer3->Add( m_Tpp1, 0, wxALL, 5 );
	
	m_GenPower = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("4250"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_GenPower, 0, wxALL, 5 );
	
	m_Thz = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("电网频率[Hz]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Thz->Wrap( -1 );
	fgSizer3->Add( m_Thz, 0, wxALL, 5 );
	
	m_hz = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("50"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_hz, 0, wxALL, 5 );
	
	m_Thz1 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("额定频率[Hz]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Thz1->Wrap( -1 );
	fgSizer3->Add( m_Thz1, 0, wxALL, 5 );
	
	m_edhz = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("48.9"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_edhz, 0, wxALL, 5 );
	
	m_staticText212 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("变流器效率"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText212->Wrap( -1 );
	fgSizer3->Add( m_staticText212, 0, wxALL, 5 );
	
	m_XiaoLv = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("0.97"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_XiaoLv, 0, wxALL, 5 );
	
	m_staticText2121 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("电机效率"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2121->Wrap( -1 );
	fgSizer3->Add( m_staticText2121, 0, wxALL, 5 );
	
	m_XiaoLvGen = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("0.97"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_XiaoLvGen, 0, wxALL, 5 );
	
	m_staticText20 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("发电机额定电压[V]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText20->Wrap( -1 );
	fgSizer3->Add( m_staticText20, 0, wxALL, 5 );
	
	m_RateVolt = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("750"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_RateVolt, 0, wxALL, 5 );
	
	m_staticText21 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("电网电压[V]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText21->Wrap( -1 );
	fgSizer3->Add( m_staticText21, 0, wxALL, 5 );
	
	m_GridVRMS = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("690"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_GridVRMS, 0, wxALL, 5 );
	
	m_Vdc2111 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)发电机额定电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Vdc2111->Wrap( -1 );
	fgSizer3->Add( m_Vdc2111, 0, wxALL, 5 );
	
	m_RateGenCurrent = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("3895"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_RateGenCurrent, 0, wxALL, 5 );
	
	m_Vdc211 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)额定直流母线电压[V]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Vdc211->Wrap( -1 );
	fgSizer3->Add( m_Vdc211, 0, wxALL, 5 );
	
	m_Vdc = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("1120"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_Vdc, 0, wxALL, 5 );
	
	m_SetNetMaxI11 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)网侧变流器额定电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetNetMaxI11->Wrap( -1 );
	fgSizer3->Add( m_SetNetMaxI11, 0, wxALL, 5 );
	
	m_SetNetCurRate = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("3456"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetNetCurRate, 0, wxALL, 5 );
	
	m_SetNetMaxI1 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)网侧变流器极限电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetNetMaxI1->Wrap( -1 );
	fgSizer3->Add( m_SetNetMaxI1, 0, wxALL, 5 );
	
	m_SetNetCurMax = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("4446"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetNetCurMax, 0, wxALL, 5 );
	
	m_SetGenMaxI111 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)机侧变流器额定电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetGenMaxI111->Wrap( -1 );
	fgSizer3->Add( m_SetGenMaxI111, 0, wxALL, 5 );
	
	m_SetGenCurRate = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("3815"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetGenCurRate, 0, wxALL, 5 );
	
	m_SetGenMaxI11 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)机侧变流器极限电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetGenMaxI11->Wrap( -1 );
	fgSizer3->Add( m_SetGenMaxI11, 0, wxALL, 5 );
	
	m_SetGenCurMax = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("4440"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetGenCurMax, 0, wxALL, 5 );
	
	m_SetSatMaxI1111 = new wxStaticText( m_scrolledWindow2, wxID_ANY, wxT("(选填)发电机定子极限电流[A]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_SetSatMaxI1111->Wrap( -1 );
	fgSizer3->Add( m_SetSatMaxI1111, 0, wxALL, 5 );
	
	m_SetSatMaxI = new wxTextCtrl( m_scrolledWindow2, wxID_ANY, wxT("1503"), wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer3->Add( m_SetSatMaxI, 0, wxALL, 5 );
	
	
	m_scrolledWindow2->SetSizer( fgSizer3 );
	m_scrolledWindow2->Layout();
	fgSizer3->Fit( m_scrolledWindow2 );
	bSizer51->Add( m_scrolledWindow2, 1, wxEXPAND | wxALL, 5 );
	
	m_checkBox1 = new wxCheckBox( this, wxID_ANY, wxT("输入激磁电抗、定子漏抗、转子漏抗折算"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer51->Add( m_checkBox1, 0, wxALL, 5 );
	
	wxFlexGridSizer* fgSizer31;
	fgSizer31 = new wxFlexGridSizer( 0, 5, 0, 0 );
	fgSizer31->SetFlexibleDirection( wxBOTH );
	fgSizer31->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	wxBoxSizer* bSizer13;
	bSizer13 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText221 = new wxStaticText( this, wxID_ANY, wxT("定子电组[ohm]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText221->Wrap( -1 );
	bSizer13->Add( m_staticText221, 0, wxALL, 5 );
	
	m_Rs = new wxTextCtrl( this, wxID_ANY, wxT("6.67E-4"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer13->Add( m_Rs, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer13, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer131;
	bSizer131 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText2211 = new wxStaticText( this, wxID_ANY, wxT("转子电阻[ohm]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2211->Wrap( -1 );
	bSizer131->Add( m_staticText2211, 0, wxALL, 5 );
	
	m_Rr = new wxTextCtrl( this, wxID_ANY, wxT("6.33E-4"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer131->Add( m_Rr, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer131, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer132;
	bSizer132 = new wxBoxSizer( wxVERTICAL );
	
	m_Lksss = new wxStaticText( this, wxID_ANY, wxT("定子漏感[H]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Lksss->Wrap( -1 );
	bSizer132->Add( m_Lksss, 0, wxALL, 5 );
	
	m_Lks = new wxTextCtrl( this, wxID_ANY, wxT("4.67E-5"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer132->Add( m_Lks, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer132, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer133;
	bSizer133 = new wxBoxSizer( wxVERTICAL );
	
	m_Lkrrr = new wxStaticText( this, wxID_ANY, wxT("转子漏感[H]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_Lkrrr->Wrap( -1 );
	bSizer133->Add( m_Lkrrr, 0, wxALL, 5 );
	
	m_Lkr = new wxTextCtrl( this, wxID_ANY, wxT("3.47E-5"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer133->Add( m_Lkr, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer133, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer101;
	bSizer101 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText22 = new wxStaticText( this, wxID_ANY, wxT("电机互感[H]"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText22->Wrap( -1 );
	bSizer101->Add( m_staticText22, 0, wxALL, 5 );
	
	m_Lm = new wxTextCtrl( this, wxID_ANY, wxT("1.01E-3"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer101->Add( m_Lm, 0, wxALL, 5 );
	
	
	fgSizer31->Add( bSizer101, 1, wxEXPAND, 5 );
	
	
	bSizer51->Add( fgSizer31, 0, 0, 5 );
	
	m_staticText1711 = new wxStaticText( this, wxID_ANY, wxT("转矩曲线表"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText1711->Wrap( -1 );
	bSizer51->Add( m_staticText1711, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_grid2 = new wxGrid( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	
	// Grid
	m_grid2->CreateGrid( 4, 26 );
	m_grid2->EnableEditing( true );
	m_grid2->EnableGridLines( true );
	m_grid2->SetGridLineColour( wxSystemSettings::GetColour( wxSYS_COLOUR_APPWORKSPACE ) );
	m_grid2->EnableDragGridSize( false );
	m_grid2->SetMargins( 0, 0 );
	
	// Columns
	m_grid2->EnableDragColMove( false );
	m_grid2->EnableDragColSize( true );
	m_grid2->SetColLabelSize( 20 );
	m_grid2->SetColLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Rows
	m_grid2->EnableDragRowSize( true );
	m_grid2->SetRowLabelSize( 80 );
	m_grid2->SetRowLabelAlignment( wxALIGN_CENTRE, wxALIGN_CENTRE );
	
	// Label Appearance
	
	// Cell Defaults
	m_grid2->SetDefaultCellAlignment( wxALIGN_LEFT, wxALIGN_TOP );
	bSizer51->Add( m_grid2, 1, wxALL|wxEXPAND, 5 );
	
	m_staticText63 = new wxStaticText( this, wxID_ANY, wxT("磁链给定说明：弱磁区间，可手动给定磁链参数。如为“空白”或“0”则根据空载开路电压计算。"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText63->Wrap( -1 );
	bSizer51->Add( m_staticText63, 0, wxALL, 5 );
	
	wxGridSizer* gSizer5;
	gSizer5 = new wxGridSizer( 1, 3, 0, 0 );
	
	wxBoxSizer* bSizer134;
	bSizer134 = new wxBoxSizer( wxVERTICAL );
	
	m_textCtrlS = new wxTextCtrl( this, wxID_ANY, wxT("550"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer134->Add( m_textCtrlS, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	m_staticText171 = new wxStaticText( this, wxID_ANY, wxT("右侧计算使用的转速点[RPM]"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText171->Wrap( -1 );
	bSizer134->Add( m_staticText171, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );
	
	
	gSizer5->Add( bSizer134, 1, wxEXPAND, 5 );
	
	m_button = new wxButton( this, wxID_ANY, wxT("重新单点计算"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer5->Add( m_button, 1, wxALL|wxEXPAND, 5 );
	
	m_button2 = new wxButton( this, wxID_ANY, wxT("报告生成"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer5->Add( m_button2, 1, wxALL|wxEXPAND, 5 );
	
	
	bSizer51->Add( gSizer5, 1, wxEXPAND, 5 );
	
	
	bSizer5->Add( bSizer51, 1, wxEXPAND, 5 );
	
	
	gSizer3->Add( bSizer5, 1, wxEXPAND, 5 );
	
	wxBoxSizer* bSizer7;
	bSizer7 = new wxBoxSizer( wxVERTICAL );
	
	m_staticText16 = new wxStaticText( this, wxID_ANY, wxT("计算结果(转速点)"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText16->Wrap( -1 );
	m_staticText16->SetFont( wxFont( 18, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("宋体") ) );
	
	bSizer7->Add( m_staticText16, 0, wxALL|wxEXPAND, 5 );
	
	m_scrolledWindow1 = new wxScrolledWindow( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow1->SetScrollRate( 5, 5 );
	wxBoxSizer* bSizer71;
	bSizer71 = new wxBoxSizer( wxVERTICAL );
	
	wxFlexGridSizer* fgSizer4;
	fgSizer4 = new wxFlexGridSizer( 0, 2, 0, 0 );
	fgSizer4->SetFlexibleDirection( wxBOTH );
	fgSizer4->SetNonFlexibleGrowMode( wxFLEX_GROWMODE_SPECIFIED );
	
	m_staticTextV = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("V:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextV->Wrap( -1 );
	fgSizer4->Add( m_staticTextV, 0, wxALL, 5 );
	
	m_V = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_V, 0, wxALL, 5 );
	
	m_staticTextW = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("W:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextW->Wrap( -1 );
	fgSizer4->Add( m_staticTextW, 0, wxALL, 5 );
	
	m_W = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_W, 0, wxALL, 5 );
	
	m_staticTextQ = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("Q:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextQ->Wrap( -1 );
	fgSizer4->Add( m_staticTextQ, 0, wxALL, 5 );
	
	m_Q = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_Q, 0, wxALL, 5 );
	
	m_staticTextR = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("R:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextR->Wrap( -1 );
	fgSizer4->Add( m_staticTextR, 0, wxALL, 5 );
	
	m_R = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_R, 0, wxALL, 5 );
	
	m_staticTextX = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("X:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextX->Wrap( -1 );
	fgSizer4->Add( m_staticTextX, 0, wxALL, 5 );
	
	m_X = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_X, 0, wxALL, 5 );
	
	m_staticTextZ = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("Z:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextZ->Wrap( -1 );
	fgSizer4->Add( m_staticTextZ, 0, wxALL, 5 );
	
	m_Z = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_Z, 0, wxALL, 5 );
	
	m_staticTextAB = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AB:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAB->Wrap( -1 );
	fgSizer4->Add( m_staticTextAB, 0, wxALL, 5 );
	
	m_AB = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AB, 0, wxALL, 5 );
	
	m_staticTextAD = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AD:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAD->Wrap( -1 );
	fgSizer4->Add( m_staticTextAD, 0, wxALL, 5 );
	
	m_AD = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AD, 0, wxALL, 5 );
	
	m_staticTextAF = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AF:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAF->Wrap( -1 );
	fgSizer4->Add( m_staticTextAF, 0, wxALL, 5 );
	
	m_AF = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AF, 0, wxALL, 5 );
	
	m_staticTextAH = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AH:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAH->Wrap( -1 );
	fgSizer4->Add( m_staticTextAH, 0, wxALL, 5 );
	
	m_AH = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AH, 0, wxALL, 5 );
	
	m_staticTextAJ = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AJ:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAJ->Wrap( -1 );
	fgSizer4->Add( m_staticTextAJ, 0, wxALL, 5 );
	
	m_AJ = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AJ, 0, wxALL, 5 );
	
	m_staticTextAK = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AK:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAK->Wrap( -1 );
	fgSizer4->Add( m_staticTextAK, 0, wxALL, 5 );
	
	m_AK = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AK, 0, wxALL, 5 );
	
	m_staticTextAL = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AL:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAL->Wrap( -1 );
	fgSizer4->Add( m_staticTextAL, 0, wxALL, 5 );
	
	m_AL = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AL, 0, wxALL, 5 );
	
	m_staticTextAM = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AM:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAM->Wrap( -1 );
	fgSizer4->Add( m_staticTextAM, 0, wxALL, 5 );
	
	m_AM = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AM, 0, wxALL, 5 );
	
	m_staticText441 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText441->Wrap( -1 );
	fgSizer4->Add( m_staticText441, 0, wxALL, 5 );
	
	m_staticText442 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText442->Wrap( -1 );
	fgSizer4->Add( m_staticText442, 0, wxALL, 5 );
	
	m_staticTextT = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("T:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextT->Wrap( -1 );
	fgSizer4->Add( m_staticTextT, 0, wxALL, 5 );
	
	m_T = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_T, 0, wxALL, 5 );
	
	m_staticTextU = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("U:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextU->Wrap( -1 );
	fgSizer4->Add( m_staticTextU, 0, wxALL, 5 );
	
	m_U = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_U, 0, wxALL, 5 );
	
	m_staticTextY = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("Y:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextY->Wrap( -1 );
	fgSizer4->Add( m_staticTextY, 0, wxALL, 5 );
	
	m_Y = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_Y, 0, wxALL, 5 );
	
	m_staticTextAA = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AA:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAA->Wrap( -1 );
	fgSizer4->Add( m_staticTextAA, 0, wxALL, 5 );
	
	m_AA = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AA, 0, wxALL, 5 );
	
	m_staticTextAC = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AC:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAC->Wrap( -1 );
	fgSizer4->Add( m_staticTextAC, 0, wxALL, 5 );
	
	m_AC = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AC, 0, wxALL, 5 );
	
	m_staticTextAE = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AE:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAE->Wrap( -1 );
	fgSizer4->Add( m_staticTextAE, 0, wxALL, 5 );
	
	m_AE = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AE, 0, wxALL, 5 );
	
	m_staticTextAG = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AG:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAG->Wrap( -1 );
	fgSizer4->Add( m_staticTextAG, 0, wxALL, 5 );
	
	m_AG = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AG, 0, wxALL, 5 );
	
	m_staticTextAI = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AI:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAI->Wrap( -1 );
	fgSizer4->Add( m_staticTextAI, 0, wxALL, 5 );
	
	m_AI = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AI, 0, wxALL, 5 );
	
	m_staticTextAN = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AN:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAN->Wrap( -1 );
	fgSizer4->Add( m_staticTextAN, 0, wxALL, 5 );
	
	m_AN = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AN, 0, wxALL, 5 );
	
	m_staticTextAO = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AO:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAO->Wrap( -1 );
	fgSizer4->Add( m_staticTextAO, 0, wxALL, 5 );
	
	m_AO = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AO, 0, wxALL, 5 );
	
	m_staticTextAP = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AP:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAP->Wrap( -1 );
	fgSizer4->Add( m_staticTextAP, 0, wxALL, 5 );
	
	m_AP = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AP, 0, wxALL, 5 );
	
	m_staticTextAQ = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AQ:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAQ->Wrap( -1 );
	fgSizer4->Add( m_staticTextAQ, 0, wxALL, 5 );
	
	m_AQ = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AQ, 0, wxALL, 5 );
	
	m_staticText4412 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText4412->Wrap( -1 );
	fgSizer4->Add( m_staticText4412, 0, wxALL, 5 );
	
	m_staticText4411 = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText4411->Wrap( -1 );
	fgSizer4->Add( m_staticText4411, 0, wxALL, 5 );
	
	m_staticTextAS = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AS:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAS->Wrap( -1 );
	fgSizer4->Add( m_staticTextAS, 0, wxALL, 5 );
	
	m_AS = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AS, 0, wxALL, 5 );
	
	m_staticTextAT = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AT:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAT->Wrap( -1 );
	fgSizer4->Add( m_staticTextAT, 0, wxALL, 5 );
	
	m_AT = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AT, 0, wxALL, 5 );
	
	m_staticTextAU = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AU:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAU->Wrap( -1 );
	fgSizer4->Add( m_staticTextAU, 0, wxALL, 5 );
	
	m_AU = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AU, 0, wxALL, 5 );
	
	m_staticTextAV = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AV:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAV->Wrap( -1 );
	fgSizer4->Add( m_staticTextAV, 0, wxALL, 5 );
	
	m_AV = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AV, 0, wxALL, 5 );
	
	m_staticTextAW = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AW:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAW->Wrap( -1 );
	fgSizer4->Add( m_staticTextAW, 0, wxALL, 5 );
	
	m_AW = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AW, 0, wxALL, 5 );
	
	m_staticTextAX = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AX:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAX->Wrap( -1 );
	fgSizer4->Add( m_staticTextAX, 0, wxALL, 5 );
	
	m_AX = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AX, 0, wxALL, 5 );
	
	m_staticTextAY = new wxStaticText( m_scrolledWindow1, wxID_ANY, wxT("AY:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticTextAY->Wrap( -1 );
	fgSizer4->Add( m_staticTextAY, 0, wxALL, 5 );
	
	m_AY = new wxTextCtrl( m_scrolledWindow1, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	fgSizer4->Add( m_AY, 0, wxALL, 5 );
	
	
	bSizer71->Add( fgSizer4, 1, wxEXPAND, 5 );
	
	
	m_scrolledWindow1->SetSizer( bSizer71 );
	m_scrolledWindow1->Layout();
	bSizer71->Fit( m_scrolledWindow1 );
	bSizer7->Add( m_scrolledWindow1, 1, wxEXPAND | wxALL, 5 );
	
	
	gSizer3->Add( bSizer7, 1, wxEXPAND, 5 );
	
	
	this->SetSizer( gSizer3 );
	this->Layout();
	m_menubar1 = new wxMenuBar( 0 );
	m_menu5 = new wxMenu();
	wxMenuItem* m_menuItem2;
	m_menuItem2 = new wxMenuItem( m_menu5, wxID_ANY, wxString( wxT("说明信息") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu5->Append( m_menuItem2 );
	
	wxMenuItem* m_menuItem3;
	m_menuItem3 = new wxMenuItem( m_menu5, wxID_ANY, wxString( wxT("版本信息") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu5->Append( m_menuItem3 );
	
	m_menubar1->Append( m_menu5, wxT("说明") ); 
	
	this->SetMenuBar( m_menubar1 );
	
	
	this->Centre( wxBOTH );
	
	// Connect Events
	m_checkBox1->Connect( wxEVT_COMMAND_CHECKBOX_CLICKED, wxCommandEventHandler( SC_CALCUL::OnCheck ), NULL, this );
	m_button->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( SC_CALCUL::m_buttonOnButtonClick ), NULL, this );
	m_button2->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( SC_CALCUL::m_buttonOnButtonClick2 ), NULL, this );
	m_menu5->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( SC_CALCUL::mOnMenuSelection2 ), this, m_menuItem2->GetId());
	m_menu5->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( SC_CALCUL::mOnMenuSelection1 ), this, m_menuItem3->GetId());
}

SC_CALCUL::~SC_CALCUL()
{
	// Disconnect Events
	m_checkBox1->Disconnect( wxEVT_COMMAND_CHECKBOX_CLICKED, wxCommandEventHandler( SC_CALCUL::OnCheck ), NULL, this );
	m_button->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( SC_CALCUL::m_buttonOnButtonClick ), NULL, this );
	m_button2->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( SC_CALCUL::m_buttonOnButtonClick2 ), NULL, this );
	
}
