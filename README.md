



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2RO2XHJ%2F20261122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261122T120632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICkUpQaDgjs81olchAUXihc30xAgoM7tTO0aAy51LZFuAiEA0%2F%2FnrFcIBosd6NrMSUAWRAcdvjZkrvlHr9wlgTDi%2F%2BEq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBF5mr1neacAr33lxCrcAyLfvVricdAyBQu%2FromfT%2FHX1gOoDylLrh6s8OEbBgmsDIRgdsVpUNu5R1Sv8PJ%2F0SI2cYsJ%2BXnjHVoaXQYbAwcvHMsOP6Kgvo9h08LEw0eWJ1RFnZ5cj6RB2eSrH83u0QsZUMvYaN8lYs6B4mBckuTVUTzRTwXHwiYn%2F8nTFhAyH7RzZosb1b0dJs3DQgVjNvBu0h11Su%2BlLJfGYs5P2iJ7Bv9ReUGMmzTnO%2FmRKNqakkBVSkKoKmTlkOkvW37CkdRYfwHi5GGKtmg9BMFYNv53eQjhdaPUolTOcDIGztq0sJX73HctfqACoPiLToCjEZhcptlf8U7UHGAHLdEbWyzhN8jioPxPxh4W%2BAajvmp9KcvHv0Jb1GPS%2FCfWiswhnt%2BImW5mlPQkj7r0bC8mVWAQPrp%2BrQ9m8u9GpI6VnLCemPEOLcMvcp0Kw6wlsIsaZqiYuo4OhhR8QZgFP2iqggJMxbKOnCnqu4ehPkaW9MVVN3IygbhUuq9oykR2CX8Dhf60ucr3yKLqouvH%2BucGdUVG018UC9QR7y6WAKsfmhrWNrscVg8tL%2BpwipWYovh6fOxv7cSfzzs01kYIWIjxrKhAPjZ5YbRlJGJ%2FzjQIppVSHY%2BdupTMY8VZ%2BdPLMLOAi9gGOqUBQ5AyH9gIjqZ2bCFbC7KYOPUXb64S3nvajHMJ1G1xkEGHB5J1JI4fw7h8rylytSpRCCf8yQKPSdEMzoadhOxVfTbLXDPxNaI1rJWM1dIFTZkL1LvpbKnhBbSS8Z7SYpQ7cI2LNG3i2b4CnQv7QOHzaUh8f1o1MvBQkP5K2yk0xW6za73HKZoSnPYjKKFt6WUUqOgUV47xlnKfbaKm0yCdEb47OgR%2B&X-Amz-Signature=5d43f2f4de01d7269ac82cc18c22d0e666d64b4c60448b21f0eb7a692afed86e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2RO2XHJ%2F20261122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261122T120632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICkUpQaDgjs81olchAUXihc30xAgoM7tTO0aAy51LZFuAiEA0%2F%2FnrFcIBosd6NrMSUAWRAcdvjZkrvlHr9wlgTDi%2F%2BEq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBF5mr1neacAr33lxCrcAyLfvVricdAyBQu%2FromfT%2FHX1gOoDylLrh6s8OEbBgmsDIRgdsVpUNu5R1Sv8PJ%2F0SI2cYsJ%2BXnjHVoaXQYbAwcvHMsOP6Kgvo9h08LEw0eWJ1RFnZ5cj6RB2eSrH83u0QsZUMvYaN8lYs6B4mBckuTVUTzRTwXHwiYn%2F8nTFhAyH7RzZosb1b0dJs3DQgVjNvBu0h11Su%2BlLJfGYs5P2iJ7Bv9ReUGMmzTnO%2FmRKNqakkBVSkKoKmTlkOkvW37CkdRYfwHi5GGKtmg9BMFYNv53eQjhdaPUolTOcDIGztq0sJX73HctfqACoPiLToCjEZhcptlf8U7UHGAHLdEbWyzhN8jioPxPxh4W%2BAajvmp9KcvHv0Jb1GPS%2FCfWiswhnt%2BImW5mlPQkj7r0bC8mVWAQPrp%2BrQ9m8u9GpI6VnLCemPEOLcMvcp0Kw6wlsIsaZqiYuo4OhhR8QZgFP2iqggJMxbKOnCnqu4ehPkaW9MVVN3IygbhUuq9oykR2CX8Dhf60ucr3yKLqouvH%2BucGdUVG018UC9QR7y6WAKsfmhrWNrscVg8tL%2BpwipWYovh6fOxv7cSfzzs01kYIWIjxrKhAPjZ5YbRlJGJ%2FzjQIppVSHY%2BdupTMY8VZ%2BdPLMLOAi9gGOqUBQ5AyH9gIjqZ2bCFbC7KYOPUXb64S3nvajHMJ1G1xkEGHB5J1JI4fw7h8rylytSpRCCf8yQKPSdEMzoadhOxVfTbLXDPxNaI1rJWM1dIFTZkL1LvpbKnhBbSS8Z7SYpQ7cI2LNG3i2b4CnQv7QOHzaUh8f1o1MvBQkP5K2yk0xW6za73HKZoSnPYjKKFt6WUUqOgUV47xlnKfbaKm0yCdEb47OgR%2B&X-Amz-Signature=9a77b2c88f29cbeddc34da085f9ebc89ced8d84ed31b682dbd5b3b25c096a020&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







