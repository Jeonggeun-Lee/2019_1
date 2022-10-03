void goForward(float second)
{
  digitalWrite(2,HIGH);
  digitalWrite(7,HIGH);
  delay((int)(second*1000.0F));
  digitalWrite(2,LOW);
  digitalWrite(7,LOW);
}

void turnLeft(float second)
{
  digitalWrite(3,HIGH);
  digitalWrite(7,HIGH);
  delay((int)(second*1000.0F));
  digitalWrite(3,LOW);
  digitalWrite(7,LOW);
}

void turnRight(float second)
{
  digitalWrite(2,HIGH);
  digitalWrite(4,HIGH);
  delay((int)(second*1000.0F));
  digitalWrite(2,LOW);
  digitalWrite(4,LOW);
}

void delaySec(float second)
{
  delay((int)(second*1000.0F));
}

void go(int times)
{
  for(int i=1 ; i<=times; i++){
    goForward(1.206);
    turnRight(0.430);
  }
}

void setup() 
{
} 
 
void loop() 
{
  delaySec(2.5);
  go(15);
}
