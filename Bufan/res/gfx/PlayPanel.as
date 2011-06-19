import flash.external.*


function onBreakClicked(e:Object)
{
	ExternalInterface.call("GameManager.Break");
}


btn_break.disableFocus = true;
btn_break.label = "认输";
btn_break.addEventListener("click", this, "onBreakClicked");



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

function SetScore(which:Number, score:Number)
{
	if(which == 0)
		lbl_val_this_score.text = score;
	else
		lbl_val_that_score.text = score;
}

function SetCountDownTime(time:Number)
{
	lbl_countDownTime.text = time;
}

