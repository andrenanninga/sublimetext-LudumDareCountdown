LudumDareCountdown
==============================

Small sublime text package to show the countdown for Ludum Dare in the status bar.
Works with Sublime text 2 and 3

## Preview

![preview] (https://github.com/fakeyou/sublimetext-LudumDareCountdown/raw/master/preview.png)

## How to install

 - Clone or [download](https://github.com/fakeyou/sublimetext-LudumDareCountdown/archive/master.zip) git repo into your packages folder

Using [Package Control](http://wbond.net/sublime_packages/package_control):

 - Run “Package Control: Install Package” command, and find `LudumDareCountdown` package

## Settings

Example config:

```
{
	// Countdown update interval
	"LudumDareCountdown_interval": 1000,

	// Ludum Dare category
	// compo - compo countdown (48 hour)
	// jam - jam countdown (72 hour)
	"LudumDareCountdown_category": "compo"
}
```

## lowliet

Based on the plugin [StatusBarTime](https://github.com/lowliet/sublimetext-StatusBarTime) by [lowliet](https://github.com/lowliet)
