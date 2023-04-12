#include <WiFiNINA.h>

char ssid[] = "Hufflepuff";     // your network SSID (name)
char pass[] = "Episkey5972"; // your network password
int status = WL_IDLE_STATUS;  // the WiFiNINA library status

IPAddress serverIP(192, 168, 1, 101); // IP address of the server
int serverPort = 1234;                // port number of the server

WiFiClient client;

const int ENA_PIN = 7; // the Arduino pin connected to the EN1 pin L298N
const int IN1_PIN = 6; // the Arduino pin connected to the IN1 pin L298N
const int IN2_PIN = 5; // the Arduino pin connected to the IN2 pin L298N

int prox_one = 8;
int prox_one_val;

int count;

void setup()
{

  Serial.begin(9600);
  pinMode(prox_one,INPUT);
  
  pinMode(ENA_PIN, OUTPUT);
  pinMode(IN1_PIN, OUTPUT);
  pinMode(IN2_PIN, OUTPUT);
  digitalWrite(ENA_PIN, HIGH);

  // Attempt to connect to WiFi network
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(5000);
  }

  Serial.println("Connected to WiFi");

  // Attempt to connect to server
  while (!client.connect("192.168.1.101", 1234)) {
    Serial.println("Failed to connect to server");
    delay(5000);
    count = 10;
  }

  count=0;
  Serial.println("Connected to server");

  // Send data to server
  client.println("Hello, server! The Assembly Station is now connected and is up running now...!");
  
}

void loop()
{

  while (count<4)
  {

    prox_one_val = digitalRead(prox_one);

    if (prox_one_val==LOW)
    {
      //Serial.println("no box detected");
  
      // extend the actuator
      digitalWrite(IN1_PIN, LOW);
      digitalWrite(IN2_PIN, HIGH);

    }

    if (prox_one_val==HIGH)
    {

      if (count<3)  
      {
        client.println("Box Aligned");

        // stop the actuator
        digitalWrite(IN1_PIN, LOW);
        digitalWrite(IN2_PIN, LOW);

        //put code here... cmd will be sent to the upper cylinder to open and close for t seconds

        client.println("now filling the box");

        delay(8000); //since no way of ensuring the box is filled, we wait for a small time 

        digitalWrite(IN1_PIN, LOW);
        digitalWrite(IN2_PIN, HIGH);

        client.println("aligning next box.................");

        delay(8000);

        count++; // Increment count by 1

        client.print("no of boxes filled:");
        client.println(count);


        delay(1000); // Wait for 1 second

      }


      else
      {
        // retracts the actuator
        client.println("retracting the actuator");        
        digitalWrite(IN1_PIN, HIGH);
        digitalWrite(IN2_PIN, LOW);  

        client.println("Boxes ready for dispatch... Waiting for the Bot to dock...!");

        delay(20000);
        count++;  //here count should become 4


      }


    }  

  }


// Exit the program once the loop is terminated  
client.println("Sequence Terminated");
delay(1000);
exit(0);

}


