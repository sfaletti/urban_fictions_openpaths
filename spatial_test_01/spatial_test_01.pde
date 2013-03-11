size(400, 400);
String[] myRawData = loadStrings("openpaths_falets.csv");
float[][] myData = new float[myRawData.length-1][3];
println(myData.length);
for (int i=1; i<myRawData.length-1; i++) {
  String[] placeHolder = split(myRawData[i], ",");
  myData[i][0] = float(placeHolder[0]);
  myData[i][1] = float(placeHolder[1]);
  myData[i][3] = 
}
for (int i=0; i<myData.length; i++) {
  println(myData[i]);
  float xPos = map (myData[i][0], 35, 45, 0, width);
  float yPos = map(myData[i][1], -74, -73, 0, height);
  ellipse(xPos, yPos, 2, 2);
}

