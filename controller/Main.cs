using Godot;
using System;

public partial class Main : Control
{
	public enum CommandsTypes {
		Forward,
		Backward,
		Right,
		Left,
		Stop,
		RunBrush,
		StopBrush
	}

	private int _speed;
	private int _commandTime;
	[Export] public HttpRequest Request;

	public string IP;

	public int Speed { 
		get => _speed;
		set {
			if (value > 0 && value <= 255)
				_speed = value;
		}
	}

	public int CommandTime {
		get => _commandTime;
		set {
			if (value > 0)
				_commandTime = value;
		}
	}

	public void SendCommand(CommandsTypes command_type) {
		string command = "";
		switch (command_type) {
			case CommandsTypes.Forward:
				command = $"010{Speed}00000000";
			break;

			case CommandsTypes.Backward:
				command = $"060{Speed}00000000";
			break;

			case CommandsTypes.Right:
				command = $"020{Speed}00000000";
			break;

			case CommandsTypes.Left:
				command = $"0200000{Speed}0000";
			break;

			case CommandsTypes.Stop:
				command = $"03000000000000";
			break;

			case CommandsTypes.RunBrush:
				command = $"0000040{Speed}0000";
			break;

			case CommandsTypes.StopBrush:
				command = $"04000000000000";
			break;
		}

		GD.Print($"https://{IP}:8080/", $"{command}\\n{CommandTime}");
		Request.Request($"https://{IP}:8080/", null, HttpClient.Method.Post, $"{command}\\n{CommandTime}");
	}

	public void OnForwardPressed() => SendCommand(CommandsTypes.Forward);

	public void OnBackwardPressed() => SendCommand(CommandsTypes.Backward);

	public void OnLeftPressed() => SendCommand(CommandsTypes.Left);

	public void OnRightPressed() => SendCommand(CommandsTypes.Right);

	public void OnStopPressed() => SendCommand(CommandsTypes.Stop);

	public void OnRunBrushPressed() => SendCommand(CommandsTypes.RunBrush);

	public void OnStopBrushPressed() => SendCommand(CommandsTypes.StopBrush);

	public void OnCommandTimeChanged(string new_time) => CommandTime = Convert.ToInt32(new_time);

	public void OnSpeedChanged(string new_speed) => Speed = Convert.ToInt32(new_speed);

	public void OnIPChanged(string new_ip) => IP = new_ip;
}
