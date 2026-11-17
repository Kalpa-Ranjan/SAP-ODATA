



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEG3JVU%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T060813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCc9lMSkcrHMnDlkKbwmrAiSLpr1GXqMjMEglTASK6EcAIhAPPUUb3NFBzrTB0RvR1dX0LZtW2u9FP6KhOHfrZG8kd%2BKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BCeFEN7lSPTPvWDYq3APsdVXPQg0w4MlhNcv8xAPXbFq19F4s1XLyDrW6OMgX4hWXbyMgsgl5E%2Fk3ViMe0ug4EZsRhm2eiaNfz5A1g1QzqJdMLqtpCXT5jAD5AG9A8vv94uB%2Fot2N%2B1za0KGTgYhyg%2FB1Y9wVmJhd5hi%2FtrsSltKdm9JxaQ1FOT23ByxUHvPG35loq3xWGlqHzPmry95kuyP3%2BbWgI0uFDt5hil3wLPFlzVuLIioshVYJSWwpYIGwxzUlpAG8PLyBZf5n%2BwUcxQpyIhdzY9MmCNVHKMaH4GL79Msf1fMsB4C6wpSpnllkhfT2ATjSQU0tkRb04bIKghHiUJjcyv2dlMXZV2mUmKJoO%2FzWCFmyvO%2FeL%2BwD%2FYrYtL%2FBIt%2FlNhRQooXw62%2BFIweWCckJMSFxp8d6ixginxe9czsoeFLPJsTrx5qmd27tkMJNv3Wcc9aHw8A2fAE%2BM6wxrp6hFb8fmvaM45prF%2FW%2Fma%2FG3HwPovsE0x5I5932aHZ7LH9GjMDz2caAaJATmqMc6Jv%2FhGUq1WfhYZsAQ81SV0wx7oiMTGuyjsR9DKTFMZi3utFOpTDrPDVV87MSmfgtZV6RvmHw8DCEHmKThAf4Ao3x9%2FqGLNznCOw5v%2BudorpHOuhgmM0ulzDU1O%2FXBjqkAfd3I%2B7p%2BjJgmJZabRR8CJI%2Bpgyk895Uon8kVe8C4PlgSSZV1kc7ghC7FC6SFjSm5ErgKow%2FoJN7XM7pyWg2%2BpnAOkYTh3HPKLdl6EdSaBTmW6KXKIjuNCyDjWZHiHM5OccHJFZj7AwZnWK2DTyo0FSsq%2Fku1jh4Q9H1mwZybWbM8Wdjo4%2FxYcDDEXkPpb0LYpaquTAjyxJNYHfH4D6nB1Zv538m&X-Amz-Signature=baec233ac73513e48c2bf881deed2b4e08ad1d5dddd666c1158845a7130aff88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AEG3JVU%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T060813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCc9lMSkcrHMnDlkKbwmrAiSLpr1GXqMjMEglTASK6EcAIhAPPUUb3NFBzrTB0RvR1dX0LZtW2u9FP6KhOHfrZG8kd%2BKogECN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2BCeFEN7lSPTPvWDYq3APsdVXPQg0w4MlhNcv8xAPXbFq19F4s1XLyDrW6OMgX4hWXbyMgsgl5E%2Fk3ViMe0ug4EZsRhm2eiaNfz5A1g1QzqJdMLqtpCXT5jAD5AG9A8vv94uB%2Fot2N%2B1za0KGTgYhyg%2FB1Y9wVmJhd5hi%2FtrsSltKdm9JxaQ1FOT23ByxUHvPG35loq3xWGlqHzPmry95kuyP3%2BbWgI0uFDt5hil3wLPFlzVuLIioshVYJSWwpYIGwxzUlpAG8PLyBZf5n%2BwUcxQpyIhdzY9MmCNVHKMaH4GL79Msf1fMsB4C6wpSpnllkhfT2ATjSQU0tkRb04bIKghHiUJjcyv2dlMXZV2mUmKJoO%2FzWCFmyvO%2FeL%2BwD%2FYrYtL%2FBIt%2FlNhRQooXw62%2BFIweWCckJMSFxp8d6ixginxe9czsoeFLPJsTrx5qmd27tkMJNv3Wcc9aHw8A2fAE%2BM6wxrp6hFb8fmvaM45prF%2FW%2Fma%2FG3HwPovsE0x5I5932aHZ7LH9GjMDz2caAaJATmqMc6Jv%2FhGUq1WfhYZsAQ81SV0wx7oiMTGuyjsR9DKTFMZi3utFOpTDrPDVV87MSmfgtZV6RvmHw8DCEHmKThAf4Ao3x9%2FqGLNznCOw5v%2BudorpHOuhgmM0ulzDU1O%2FXBjqkAfd3I%2B7p%2BjJgmJZabRR8CJI%2Bpgyk895Uon8kVe8C4PlgSSZV1kc7ghC7FC6SFjSm5ErgKow%2FoJN7XM7pyWg2%2BpnAOkYTh3HPKLdl6EdSaBTmW6KXKIjuNCyDjWZHiHM5OccHJFZj7AwZnWK2DTyo0FSsq%2Fku1jh4Q9H1mwZybWbM8Wdjo4%2FxYcDDEXkPpb0LYpaquTAjyxJNYHfH4D6nB1Zv538m&X-Amz-Signature=9508378f544758b9721b1f53331a338c26b3709b9e0c38d16e6fe3731b1b15c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







