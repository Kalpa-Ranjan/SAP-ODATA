



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMMBH7C4%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T124346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZBcncEotr22BI%2BihQDQecTGZHBAjvBLdqwQeycpyGdQIhAPpPdBOdz0YBRF5UliOMxQZZXqeK%2FRSeWAT4Qmk6FGYDKogECLb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVf%2Fa3W9U%2Bvs77riMq3AOwURQYc2vEEW43mObgxNcM9o8Sb2HygdJ%2Bs3ekntBQ6b87cFy1ac2BJEJUMAhRgeGnv9UNpP2l9861HLbAl3fUkRk5f9Tv%2BiMCJxH7%2F433l5jZJE%2B6rp%2BYBgRXGp7v%2BcLrF7w%2BmdKy2mPgQyeatx8LoZlXcjIoWEsyAMkeeh3VPjoYr6N%2BRXL%2FAlbOZMjtfKkzDQNCdjYwmmTSoAMyBT0wr%2Bn9T499Odn14oSyb%2FPyiiCakuAvXfVD9kCe58YEqQrbaOdQ%2FczK1HAjWZ3wRvpY7ObD8RZ7hkE7ojv3hGwgl%2B4%2FU%2FB8Ni%2BntZCMg%2F76HtBGM%2BG6otkm8I84LQLhQi2UamFTPI19QKXJt%2FIgiMXP5YlkElIK%2F2QZYTVRdDH1s%2BhF9qDv0C7K55QEbjf%2B3CFD2fUCZPFTxaV9i8zdPczvwWXx0gks6g7tGDoZvFhYmK8z0Rh%2FIvoVn6uNhcyYzM0%2BDyAnHK6cChzEDXrio3nuKv27PWGCCLZ1Uevrrk2Xrpw2mC25UmilsKj6dnC8A9uzJQG1OmGg4i08RaLDeR2UUGU6Cr7DgJT9DkI2sx%2FzNnGiZed6IOgyN8Nm6M35CYOnJNkakB2ipc%2BlV0xVRzp3ynOm5sOy%2BfEuS%2BrnADDQzKDNBjqkATUnNbeqcPcSUas2biOcrknC6oBubV02msOqYspTgYLbCriFrMOpxeP73ePa632cePyvDEheqxmMODAK5Y%2Fno9R5P3kUeUQWh8uUlqzbvwU1jbuxvoQpA0u7jDKE4AaRlHhzVsO01wc0ZPPU5jrIPAVzWZ3wwQkckPGA0fqvDvAgQo8mXDDg927Ou67uxyLQNNHPkbkDuRujuI9k4aK46H5eUCHg&X-Amz-Signature=ca9b54ab6ac7a12b4d11dae14a317a1f21606fe3e3aed66e95a0d67d6e2144be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMMBH7C4%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T124346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZBcncEotr22BI%2BihQDQecTGZHBAjvBLdqwQeycpyGdQIhAPpPdBOdz0YBRF5UliOMxQZZXqeK%2FRSeWAT4Qmk6FGYDKogECLb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVf%2Fa3W9U%2Bvs77riMq3AOwURQYc2vEEW43mObgxNcM9o8Sb2HygdJ%2Bs3ekntBQ6b87cFy1ac2BJEJUMAhRgeGnv9UNpP2l9861HLbAl3fUkRk5f9Tv%2BiMCJxH7%2F433l5jZJE%2B6rp%2BYBgRXGp7v%2BcLrF7w%2BmdKy2mPgQyeatx8LoZlXcjIoWEsyAMkeeh3VPjoYr6N%2BRXL%2FAlbOZMjtfKkzDQNCdjYwmmTSoAMyBT0wr%2Bn9T499Odn14oSyb%2FPyiiCakuAvXfVD9kCe58YEqQrbaOdQ%2FczK1HAjWZ3wRvpY7ObD8RZ7hkE7ojv3hGwgl%2B4%2FU%2FB8Ni%2BntZCMg%2F76HtBGM%2BG6otkm8I84LQLhQi2UamFTPI19QKXJt%2FIgiMXP5YlkElIK%2F2QZYTVRdDH1s%2BhF9qDv0C7K55QEbjf%2B3CFD2fUCZPFTxaV9i8zdPczvwWXx0gks6g7tGDoZvFhYmK8z0Rh%2FIvoVn6uNhcyYzM0%2BDyAnHK6cChzEDXrio3nuKv27PWGCCLZ1Uevrrk2Xrpw2mC25UmilsKj6dnC8A9uzJQG1OmGg4i08RaLDeR2UUGU6Cr7DgJT9DkI2sx%2FzNnGiZed6IOgyN8Nm6M35CYOnJNkakB2ipc%2BlV0xVRzp3ynOm5sOy%2BfEuS%2BrnADDQzKDNBjqkATUnNbeqcPcSUas2biOcrknC6oBubV02msOqYspTgYLbCriFrMOpxeP73ePa632cePyvDEheqxmMODAK5Y%2Fno9R5P3kUeUQWh8uUlqzbvwU1jbuxvoQpA0u7jDKE4AaRlHhzVsO01wc0ZPPU5jrIPAVzWZ3wwQkckPGA0fqvDvAgQo8mXDDg927Ou67uxyLQNNHPkbkDuRujuI9k4aK46H5eUCHg&X-Amz-Signature=f7076bf5219aa90cee48aaa59d6a8a28c1f9d90be42bd7fa068629018700e2d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







