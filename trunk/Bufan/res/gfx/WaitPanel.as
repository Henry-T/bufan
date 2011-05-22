import flash.external.*

function onLeaveClicked(e:Object)
{
	ExternalInterface.call("InGame.RequestLeaveRoom");
}

function onReadyClicked(e:Object)
{
	ExternalInterface.call("InGame.GetReady");
}

btn_leave.disableFocus = true;
btn_leave.label = "退出";
btn_leave.addEventListener("click", this, "onLeaveClicked");

btn_ready.disableFocus = true;
btn_ready.label = "准备";
btn_ready.addEventListener("click", this, "onReadyClicked");


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

