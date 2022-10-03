                
// 아두이노 보드에서 사용할 핀을 설정합니다.
//2,3,7,4,5,6// 좌측모터 전진2,좌측모터 후진3,우측모터 전진7,좌측 후진4,좌측PWM,우측PWM

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
    turnRight(0.448);
  }
}

void setup() 
{
} 
 
void loop() 
{
  delaySec(2.5);
  go(5);
  turnLeft(1.168);
  go(8);
  turnRight(1.301);
  go(7);
}
