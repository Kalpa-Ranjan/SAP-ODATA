



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CBADHWU%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T125656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGQdv9SOGJ2stIYP4S9rU9WtwKfjXF%2FLzh6nQNsTjR2SAiEA4Tdnwng5QDV2O9UXe8rkjn1E%2Bx4L239jaPcOB3GHKf0qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG%2B%2BFL%2F9oNnGHEQ%2BSrcA%2By3hX2pYWUISAcBovjtm%2Bl9nBftECNMYY0IjLa6KK3drenII6kN6UUjSbGgZBFuwFnyZ1Eb31XfLGPK7HWjWgexEPSagS%2BcbaTfDYrYosbpHyhuiI4yAdymA2kIOBOiqbIy00hLt7WboeGmJFTWSR3dW6vuOPgRhG591AmJO6chju%2FeX4L0NgOkDd6QT4fdi0zsTdhlOAzVaATBcqHVYOGdWwvW2RC4wm9Wu3cTB2mhk7EWNSrK9qcJ6LJKS7k4UPY%2BGqQWEo0tf%2FLj8Iq%2Bg7IlCpFal4VknwgUf1rTBkccJmoIK6o3fPKW25n0CVmbHAzS%2BNWi0vyqf%2FNrLXZQKIQZPYrL9ElJdx20u4%2FUwYKlhrgCjG1s4j%2BgwyJWgwEK%2BSiasifFH%2FISfeSc7J3rZ0vPnX2ftYhm5EW3qUUZtn459L4LM4XDLaCiyE7Gifqa7eXHvfhHoOBC0keZtB92xX1A8hZxNfKU9acMpdgAWDw%2Be8mRp0qh13oBCBw2v59L91nzAM0IdbO%2BN8p3ACRl%2FgynM1Q0qs9i3K3gClrP%2Bz04Xm6vX4EtuOMRg2%2F9CwBLScmlT3i%2FEYrTN4geHMQb9dX0qno0QrNHaM0cgSE1ECi3f8tWWjv8%2FpA1puzZMNTW9tMGOqUBagqC8RbW1UIRISryPYAftyOgAOPbTPjcs43JDohV3rKRyW2XqRuqYEPvGDX4gFBM3WkMoxZapVWP4Ba7HIhgh2TXc2WueGQwvbCBfHhF5SahKNjBTYaDrq25fQlhYcFxCCVGTDzUOG29059lBzfS26zhqfXKQhPHc9x356dpB9JaKvZHuA6JaRMPZq2rpCKvOVHuw9DllORT7w%2FN0Fcco7j2BIi7&X-Amz-Signature=e3a52d1025965c50b9135c49f9265e015195a8cf93d4893ff782ae12c472f2f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CBADHWU%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T125657Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGQdv9SOGJ2stIYP4S9rU9WtwKfjXF%2FLzh6nQNsTjR2SAiEA4Tdnwng5QDV2O9UXe8rkjn1E%2Bx4L239jaPcOB3GHKf0qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBG%2B%2BFL%2F9oNnGHEQ%2BSrcA%2By3hX2pYWUISAcBovjtm%2Bl9nBftECNMYY0IjLa6KK3drenII6kN6UUjSbGgZBFuwFnyZ1Eb31XfLGPK7HWjWgexEPSagS%2BcbaTfDYrYosbpHyhuiI4yAdymA2kIOBOiqbIy00hLt7WboeGmJFTWSR3dW6vuOPgRhG591AmJO6chju%2FeX4L0NgOkDd6QT4fdi0zsTdhlOAzVaATBcqHVYOGdWwvW2RC4wm9Wu3cTB2mhk7EWNSrK9qcJ6LJKS7k4UPY%2BGqQWEo0tf%2FLj8Iq%2Bg7IlCpFal4VknwgUf1rTBkccJmoIK6o3fPKW25n0CVmbHAzS%2BNWi0vyqf%2FNrLXZQKIQZPYrL9ElJdx20u4%2FUwYKlhrgCjG1s4j%2BgwyJWgwEK%2BSiasifFH%2FISfeSc7J3rZ0vPnX2ftYhm5EW3qUUZtn459L4LM4XDLaCiyE7Gifqa7eXHvfhHoOBC0keZtB92xX1A8hZxNfKU9acMpdgAWDw%2Be8mRp0qh13oBCBw2v59L91nzAM0IdbO%2BN8p3ACRl%2FgynM1Q0qs9i3K3gClrP%2Bz04Xm6vX4EtuOMRg2%2F9CwBLScmlT3i%2FEYrTN4geHMQb9dX0qno0QrNHaM0cgSE1ECi3f8tWWjv8%2FpA1puzZMNTW9tMGOqUBagqC8RbW1UIRISryPYAftyOgAOPbTPjcs43JDohV3rKRyW2XqRuqYEPvGDX4gFBM3WkMoxZapVWP4Ba7HIhgh2TXc2WueGQwvbCBfHhF5SahKNjBTYaDrq25fQlhYcFxCCVGTDzUOG29059lBzfS26zhqfXKQhPHc9x356dpB9JaKvZHuA6JaRMPZq2rpCKvOVHuw9DllORT7w%2FN0Fcco7j2BIi7&X-Amz-Signature=042c212d676dcac08123ce4b4850a3cf9c2f321476814bf8d90a33a0957bf51e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







