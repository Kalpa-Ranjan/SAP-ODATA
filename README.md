



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC2B4FVO%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T182453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD50nz%2Byr%2BmVs%2FrGdBuv0tHFqXzlz%2F0J5H%2FgYGfTk4ooAIgE0i0TRM8CUqLJGosadvOYuoeLW0WovZD4R4p2YI4QqIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJhzAIQ1xySEdlbnaircAxe9LADoaUH8ho8hCYgkn9bFNX8vOzguJCZLvb%2FFq7nl3Pi6gDZy3SfPX6p%2BZ1B5Ydo7jIgh0ACDvJV6TJ1NgHSOA4yfvFzvBwnrRvMyjySSTDrWVofqXNq6TaJQi3il9TgJnXzbLtUTAPgbVJKW%2BMzKIJvvG0wFsHHMnKap5k8JLkXla0FMxNslYdwPM5zY%2Bo8rRybuclGbzf8EyPa0fXSE2Z5Er1gLrddcRGJD%2FCKT4NL%2F2MVTCcZL62%2Bt0ft0f%2FXjier4txsIbL6n6knbQzUjPC%2Fdg1zsliSEfg7ihs7a5tLBTMIvNMULtJQ7P3R2Jfbh1ntATPx2KzrzfwtIcXZ6Bp%2BerS8EYrJ4tplsLE8DYQq5yVXYX%2BkKoiFbsUQTBzmvGPI303cmoMrNtP5nYsSBtn81%2FHD1FgyK8PEezNdcGcykfI%2F4bWF72903elqsiVYWcdheg%2B%2FYByfOGQuTiq00NXNwS0lrsS4PIKnN3Y7UjS8R7vBOb8duCY6kBAeYH7wp5SydTve56azIL54495uG8KHXQJq6C8NFSk5vSVDhv8P0%2BK7OS1e7VfZ7QhASlyJ%2Btqbbb7yDVnQdqPOi2r7d8rgoEts3q8Q7FF3JkuLyk9Jbeq7mPjGDSrP3MI6IkcoGOqUBkL4NGz%2FsyExjj62aMScSKNpm9Endxvar%2Ff6d4aSZPgt2E1Vf%2FiQc4lt1bLMhK4IEJOJ4a6mmpBGc5UlzWcjS6%2Fr6sU5ZH%2BF6YlL8kNE%2BVlbQgcLRakPNxjTairuV8CXrN5v44mfSSQ4QfHZ1kajo680FRxu6lH2UBS7Kb5ZQx2q4D%2FBTKzeFBiwPMUz5n7Dq%2FWsloXzfc5O%2BdHdcQDrClfPFQieV&X-Amz-Signature=42dbe7aadd311e659092fe91808c59505e5f1831cae1c77b213f061115f002ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC2B4FVO%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T182453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD50nz%2Byr%2BmVs%2FrGdBuv0tHFqXzlz%2F0J5H%2FgYGfTk4ooAIgE0i0TRM8CUqLJGosadvOYuoeLW0WovZD4R4p2YI4QqIqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJhzAIQ1xySEdlbnaircAxe9LADoaUH8ho8hCYgkn9bFNX8vOzguJCZLvb%2FFq7nl3Pi6gDZy3SfPX6p%2BZ1B5Ydo7jIgh0ACDvJV6TJ1NgHSOA4yfvFzvBwnrRvMyjySSTDrWVofqXNq6TaJQi3il9TgJnXzbLtUTAPgbVJKW%2BMzKIJvvG0wFsHHMnKap5k8JLkXla0FMxNslYdwPM5zY%2Bo8rRybuclGbzf8EyPa0fXSE2Z5Er1gLrddcRGJD%2FCKT4NL%2F2MVTCcZL62%2Bt0ft0f%2FXjier4txsIbL6n6knbQzUjPC%2Fdg1zsliSEfg7ihs7a5tLBTMIvNMULtJQ7P3R2Jfbh1ntATPx2KzrzfwtIcXZ6Bp%2BerS8EYrJ4tplsLE8DYQq5yVXYX%2BkKoiFbsUQTBzmvGPI303cmoMrNtP5nYsSBtn81%2FHD1FgyK8PEezNdcGcykfI%2F4bWF72903elqsiVYWcdheg%2B%2FYByfOGQuTiq00NXNwS0lrsS4PIKnN3Y7UjS8R7vBOb8duCY6kBAeYH7wp5SydTve56azIL54495uG8KHXQJq6C8NFSk5vSVDhv8P0%2BK7OS1e7VfZ7QhASlyJ%2Btqbbb7yDVnQdqPOi2r7d8rgoEts3q8Q7FF3JkuLyk9Jbeq7mPjGDSrP3MI6IkcoGOqUBkL4NGz%2FsyExjj62aMScSKNpm9Endxvar%2Ff6d4aSZPgt2E1Vf%2FiQc4lt1bLMhK4IEJOJ4a6mmpBGc5UlzWcjS6%2Fr6sU5ZH%2BF6YlL8kNE%2BVlbQgcLRakPNxjTairuV8CXrN5v44mfSSQ4QfHZ1kajo680FRxu6lH2UBS7Kb5ZQx2q4D%2FBTKzeFBiwPMUz5n7Dq%2FWsloXzfc5O%2BdHdcQDrClfPFQieV&X-Amz-Signature=ec54576f4683084d1d55985924934e83991d19dc2ed4e85d1a1ca2f7ce1d0096&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







