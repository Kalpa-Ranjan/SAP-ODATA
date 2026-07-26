



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C23IY4K%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T130748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIAohORkHznn7wclnLcKSWymQnQi7mUQIUeNuSC78YvtsAiAHnRszgNRmJakHkznninNt5uWeu3soSKKPh6EZe%2BavAyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMOcWBJ5%2FFpbUJOq%2BZKtwDI2835Am2SK5BaktDjj7UgeCPBF59Y95uOIeJSuoAB7Rjk%2FzFsA1F5DQ9ildjFoDug1e3PKZgG2CRJEuqhz8uC4yY90nafgfBNEJ9DnECefmMACDp%2F%2BaLMN2o2oWdyMa7wxytA9avVDONYz2A26p0xfmjF32y4dwSWV9%2BWRFyIEc8a1QcjKR3Pw5lMCDOK93hQ9vUES5NUV6x2%2FJAuvZ%2F4bfyiiHY8zuVqNh0OuyGqnDaC2AnFMYkr6rFswM3bEIfLZidkLQ24iPdPcO5flhuM2GfrSl5dzxRGFcXjOcz4VsfEZC0oMJj7tkwcTtVXwissx9ycUvv7%2B%2Fx%2FApnahrXPIEE0aMjUuPpR5rmM%2Bwb9%2FfpW4xrF8z72cz%2Bs6RhiUqgcAxqVvXL%2BY0DndCffA%2BWDsBgwPvCIt7xm4xlEw4M%2BosIxFmzCSBtZLQHUO5tUHSMSSs6zATebYQj%2BoJmqfhrYuAFyX3L3i3ml6PfNnSYtryg9ouSPWIL3kxaqrVEnpozOAfe%2FWBlLadV4%2FjwaYXL8gin5U%2Bajb7IKp4FYtws8VL%2FjidmOg0hV954WfVyqugq19z%2Bz%2F%2Fyb99Tqoj7nwxvi9e6voVbP1Vcnn52Bu8fiAr16g3RAlzWLh%2FHAsMw4ceX0wY6pgEQXoQXAtzhAAslpyWBL5WCIJWN1HTIiYyPuZ6cJLWe0%2BYvmj%2B3EarAg5jUAZOsJkZ%2BhtyTrPij%2FBn5nNgr%2FvsMl6rU2EPh4ptydICjSn1PSE%2Fp4YCqHF125nJ5%2FzjYp1ELpxzqh3OKFwj4qT%2Fy4ajSZcIIhxEhpy%2FG%2Bxb%2FDtYC1mubiMBrL5Df8osnPENAEcWKQpWbkPZzD73xU3qTSziCQyzqemr8&X-Amz-Signature=82f0cdeb4a7b116ca35bedc236c6befb22eacb616dff14f59668e79cd9925a38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C23IY4K%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T130748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIAohORkHznn7wclnLcKSWymQnQi7mUQIUeNuSC78YvtsAiAHnRszgNRmJakHkznninNt5uWeu3soSKKPh6EZe%2BavAyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMOcWBJ5%2FFpbUJOq%2BZKtwDI2835Am2SK5BaktDjj7UgeCPBF59Y95uOIeJSuoAB7Rjk%2FzFsA1F5DQ9ildjFoDug1e3PKZgG2CRJEuqhz8uC4yY90nafgfBNEJ9DnECefmMACDp%2F%2BaLMN2o2oWdyMa7wxytA9avVDONYz2A26p0xfmjF32y4dwSWV9%2BWRFyIEc8a1QcjKR3Pw5lMCDOK93hQ9vUES5NUV6x2%2FJAuvZ%2F4bfyiiHY8zuVqNh0OuyGqnDaC2AnFMYkr6rFswM3bEIfLZidkLQ24iPdPcO5flhuM2GfrSl5dzxRGFcXjOcz4VsfEZC0oMJj7tkwcTtVXwissx9ycUvv7%2B%2Fx%2FApnahrXPIEE0aMjUuPpR5rmM%2Bwb9%2FfpW4xrF8z72cz%2Bs6RhiUqgcAxqVvXL%2BY0DndCffA%2BWDsBgwPvCIt7xm4xlEw4M%2BosIxFmzCSBtZLQHUO5tUHSMSSs6zATebYQj%2BoJmqfhrYuAFyX3L3i3ml6PfNnSYtryg9ouSPWIL3kxaqrVEnpozOAfe%2FWBlLadV4%2FjwaYXL8gin5U%2Bajb7IKp4FYtws8VL%2FjidmOg0hV954WfVyqugq19z%2Bz%2F%2Fyb99Tqoj7nwxvi9e6voVbP1Vcnn52Bu8fiAr16g3RAlzWLh%2FHAsMw4ceX0wY6pgEQXoQXAtzhAAslpyWBL5WCIJWN1HTIiYyPuZ6cJLWe0%2BYvmj%2B3EarAg5jUAZOsJkZ%2BhtyTrPij%2FBn5nNgr%2FvsMl6rU2EPh4ptydICjSn1PSE%2Fp4YCqHF125nJ5%2FzjYp1ELpxzqh3OKFwj4qT%2Fy4ajSZcIIhxEhpy%2FG%2Bxb%2FDtYC1mubiMBrL5Df8osnPENAEcWKQpWbkPZzD73xU3qTSziCQyzqemr8&X-Amz-Signature=f3d55e9cea8232ed7a8b29b10725a71e5b8900191fe0b6b79b167a90c6ff9549&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







