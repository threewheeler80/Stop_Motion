# Stop_Motion
Initially this started as a stop motion project, growing into much more.

Hardware List
  Raspberry Pi Zero WH adafruit PID 3708
  Mini Illuminated Momentary Pushbutton Blue adafruit PID 3105
  30mm Arcade Button PID 471 clear
  30mm Arcade Button PID 473 red
  30mm Arcade Button PID 476 blue
  Perma Proto Bonnet Mini Kit PID 3203
  22 AWG stranded core PID 3175
  Multi-colored heat shrink PID 4559
  Raspberry Pi HQ Camera PID 4561
  6mm 3MP wide angle lens PID 4563
  LED sequins royal blue PID 476
  LED sequins ruby red PID 1755
  LED sequins warm white PID 1758
  Glarks 2.5mm pitch JST-SM 9 pin female/male connectors
  Glarks 2.54mm pitch JST-XHP 6 pin and 3 pin female/male connectors
  Makerele M3-180807 enclosure box
  
Ok everything works as far as the code technically!!! lol
BUT, recently advised that there should have pulldowns on the button inputs, resistors or internally with the script
Also, when pressing the preview button initially the red led sequin (image button) will illuminate for approx 3-5 seconds then go off. Press the preview button again the red sequin illuminates for approx. one second. Each subsequent press of the preview button the red led sequin quickly illuminates and then off, Odd layout?

Installed 10kohm resistors on the GPIO pins/ and 3volt, for the buttons. Noticed that the red LED sequin was dimly lit. Used isopropyl alcohol, toothbrush and compressed air to clean the perma proto bonnet... fixed. Next the python script stopped working specifically  camera initializing and saving images/video to folders. Started again on the recent script... fixed again...
