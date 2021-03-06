List2CSV-Sublime-Plugin 2.0
=======================

Plugin for creating comma separated value from a list of data

What this plugin Does ?
=======================

It's a simple utility to convert list data to csv format for example

`12321`

`45612`    `--------------->` `12321,45612,78924,12124`

`78924`

`12124`

It can be helpful for big data loaders and other process which demands a csv


How to install ?
--------------

With Package Control:

Run “Package Control: Install Package” command, find and install `list2csv` plugin.
Restart ST editor (if required)

For manual install 

* Download zip file , rename it to  <kbd>list2csv.sublime-package</kbd> file and keep it inside the installed directory
  for example "C:\Users\avagrawa\AppData\Roaming\Sublime Text 2\Installed Packages\".
*  Do a git clone in package directory:
     <kbd>git clone https://github.com/avinash8526/List2CSV-Sublime-Plugin.git<kbd>


How to use
----------


- Basic Use

If you have a list , select all and press `ctrl`+`alt`+`,` or right click on mouse and select option "Convert List To CSV"
watch a `youtube` demo on how to use it `http://www.youtube.com/watch?v=W1HLoRRxKRk

- Advance Use (New Features added for 2.0)

Change the pattern by hitting `ctrl`+`alt`+`.` , you will see input panel `{'SecondDel':'','rowlen':'NULL','Separator':',','FirstDel':'','Memory':'No','ShowPop':'Yes'}` now if you want some pattern like `"123","1234"` instead of `123,1234` then change the string as {'SecondDel':'`"`','rowlen':'NULL','Separator':',','FirstDel':'`"`','Memory':'No','ShowPop':'Yes'}. If you want to maintain the pattern for whole session change the `Memory` value from `No` to `Yes`.
Watch youtube demo [http://www.youtube.com/watch?v=PrkrRqjUoO0 ](http://www.youtube.com/watch?v=PrkrRqjUoO0 "Youtube demo") With new implementation now row length can be set by changing `NULL` by the row length `{'SecondDel':'','rowlen':'3','Separator':',','FirstDel':'','Memory':'No','ShowPop':'Yes'}` it will generate pattern in this format

- `123,123,123`
- `343,234,234`

` A pattern of 3 entity in a row`


License
-------
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">List2csv Sublime Plugin</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/avinash8526/List2CSV-Sublime-Plugin" rel="dct:source">https://github.com/avinash8526/List2CSV-Sublime-Plugin</a>.


