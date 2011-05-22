import flash.external.*

function onLeaveClicked(e:Object)
{
	ExternalInterface.call("InGame.RequestLeaveRoom");
}

btn_leave.disableFocus = true;
btn_leave.text = "认输";
btn_leave.addEventListener("click", this, "onLeaveClicked");
