import flash.external.*

var thisReady:Number = 0;

function onLeaveClicked(e:Object)
{
	ExternalInterface.call("GameManager.RequestLeaveRoom");
}

function onReadyClicked(e:Object)
{
	if(thisReady == 0)
		ExternalInterface.call("GameManager.SetReady",1);
	else
		ExternalInterface.call("GameManager.SetReady",0);
}

function UIReady(which:Number, isReady:Number)
{
	if(which == 0 && isReady == 0)
	{
		thisReady = 0;
		m_this_ready.gotoAndStop(1);
	}
	else if(which == 0 && isReady == 1)
	{
		thisReady = 1;
		m_this_ready.gotoAndStop(2);
	}
	else if(which == 1 && isReady == 0)
		m_that_ready.gotoAndStop(1);
	else if(which == 1 && isReady == 1)
		m_that_ready.gotoAndStop(2);
}

function onTrainClicked(e:Object)
{
	ExternalInterface.call("GameManager.Train");
}

btn_leave.disableFocus = true;
btn_leave.label = "退出";
btn_leave.addEventListener("click", this, "onLeaveClicked");

btn_ready.disableFocus = true;
btn_ready.label = "准备";
btn_ready.addEventListener("click", this, "onReadyClicked");

btn_train.disableFocus = true;
btn_train.label = "练习";
btn_train.addEventListener("click", this, "onTrainClicked");


function SetThisInfo(neck:String, winC:Number, drawC:Number, lose:Number, breakC:Number)
{
	lbl_val_this_neck.text = neck;
	lbl_val_this_win.text = winC.toString();
	lbl_val_this_draw.text = drawC.toString();
	lbl_val_this_lose.text = lose.toString();
	lbl_val_this_break.text = breakC.toString();
}

function SetThatInfo(neck:String, winC:Number, drawC:Number, lose:Number, breakC:Number)
{
	lbl_val_that_neck.text = neck;
	lbl_val_that_win.text = winC.toString();
	lbl_val_that_draw.text = drawC.toString();
	lbl_val_that_lose.text = lose.toString();
	lbl_val_that_break.text = breakC.toString();
}

function ClearThatInfo()
{
	lbl_val_that_neck.text = "---";
	lbl_val_that_win.text = "---";
	lbl_val_that_draw.text = "---";
	lbl_val_that_lose.text = "---";
	lbl_val_that_break.text = "---";
}

function SetTrainScore(score:Number)
{
	lbl_val_score.text = score.toString();
}