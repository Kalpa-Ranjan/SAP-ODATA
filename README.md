



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZIOQCOB%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T130517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIECZ9cph1Rr2%2BWHV3yilFG9%2Bdt%2FoVXlqgLbJZ0T0Ni4SAiAPF9tAmmOuodY0%2Bz7lZAdLBnn4Es5bAvOEXs4RwzrPUCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8U7xLNiAZIF8M7deKtwDxTULI6zDIImoBWurNQfimPukGvVexhN2XemfDrsmSvGYPvXCP08p2SYp%2BzgHxgILdGts560eOw5JJmfw%2FXhvyusybsmdM8QljwcIAGSUeIgwvk1Rh7%2Bfr4HeGg2Frlv0YDJUS8%2BOpqruvBJucpR08kuHkNLFNfMtZHflXkKQeRDgB%2B%2FUPLUcQNWK%2BQ5S5cQiyT41iG35mf5kO5k8Jamui05rlQCV%2FxCPQ0DT6jvX8KP2%2FxzpiW%2Bx4RI9HdF1S5BMjfA%2BYhZDXPUeaW%2FLL4oi%2F6Ot7bzohgpD1LyMe5BmT%2BCJbU%2FfyrK3r80DnRFNSTcXeKFef4T3kBsf3SPmtEETvAzbV7kphYqjMOwcJO28joqfvE3ljJu5JxsZGMlyCHj%2BVJk1e0fOWM%2BCgvTtiv8H6PqEZclaZ9lCGltKxO6YcxmQhNPPgjP2iZcry48Rz22gH%2Bkwr1dFeHGxh0ZdxgK6rJ5Sm6g%2FqEE1QMkDZ5yrxcNzl1ckCzkL70uWAp5pGTPMANWs7tM4Gcv1DbaVW6quj2RAFPUuy%2FPLAJ%2B7oDyMppgY1Og6hkfFgs7J7WNkFZPraa9wIkLSAoBQ4%2FQqqs8XPfSv9adf%2FwtjHvZkIFvdcNAzKexfoompXFkhA7gwuvb7zwY6pgHlXBEXERexMwNeSvK0AMifTRXUF9%2FQBWQOgX51uSVo1ouUfFOQS8sBcaRa1eLxSVxCdxxwZUH0eI1n0iOzZrE7KvZ19b2o3soqWuWMONf%2B9IGt4L%2Fez6Zm0ARhH%2FHQcnh6Vp91h4Syg6gAD54B05%2FqNWm6UZ7Ezge4eQd8ieAA%2B51EeNoVo2o%2BgRoX0cmdm8MYQXlwe8OtZ%2BFf%2FCmSxgVO21JyhRR2&X-Amz-Signature=b0c490ab5979fb782514f6df07e34e4610d0cf86123aed4951a80ad9f1a90d17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZIOQCOB%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T130517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIECZ9cph1Rr2%2BWHV3yilFG9%2Bdt%2FoVXlqgLbJZ0T0Ni4SAiAPF9tAmmOuodY0%2Bz7lZAdLBnn4Es5bAvOEXs4RwzrPUCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8U7xLNiAZIF8M7deKtwDxTULI6zDIImoBWurNQfimPukGvVexhN2XemfDrsmSvGYPvXCP08p2SYp%2BzgHxgILdGts560eOw5JJmfw%2FXhvyusybsmdM8QljwcIAGSUeIgwvk1Rh7%2Bfr4HeGg2Frlv0YDJUS8%2BOpqruvBJucpR08kuHkNLFNfMtZHflXkKQeRDgB%2B%2FUPLUcQNWK%2BQ5S5cQiyT41iG35mf5kO5k8Jamui05rlQCV%2FxCPQ0DT6jvX8KP2%2FxzpiW%2Bx4RI9HdF1S5BMjfA%2BYhZDXPUeaW%2FLL4oi%2F6Ot7bzohgpD1LyMe5BmT%2BCJbU%2FfyrK3r80DnRFNSTcXeKFef4T3kBsf3SPmtEETvAzbV7kphYqjMOwcJO28joqfvE3ljJu5JxsZGMlyCHj%2BVJk1e0fOWM%2BCgvTtiv8H6PqEZclaZ9lCGltKxO6YcxmQhNPPgjP2iZcry48Rz22gH%2Bkwr1dFeHGxh0ZdxgK6rJ5Sm6g%2FqEE1QMkDZ5yrxcNzl1ckCzkL70uWAp5pGTPMANWs7tM4Gcv1DbaVW6quj2RAFPUuy%2FPLAJ%2B7oDyMppgY1Og6hkfFgs7J7WNkFZPraa9wIkLSAoBQ4%2FQqqs8XPfSv9adf%2FwtjHvZkIFvdcNAzKexfoompXFkhA7gwuvb7zwY6pgHlXBEXERexMwNeSvK0AMifTRXUF9%2FQBWQOgX51uSVo1ouUfFOQS8sBcaRa1eLxSVxCdxxwZUH0eI1n0iOzZrE7KvZ19b2o3soqWuWMONf%2B9IGt4L%2Fez6Zm0ARhH%2FHQcnh6Vp91h4Syg6gAD54B05%2FqNWm6UZ7Ezge4eQd8ieAA%2B51EeNoVo2o%2BgRoX0cmdm8MYQXlwe8OtZ%2BFf%2FCmSxgVO21JyhRR2&X-Amz-Signature=a39e51f0a882921b1fbdcf9dafff8047f307f354918e72b0547949f56db1ad66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







