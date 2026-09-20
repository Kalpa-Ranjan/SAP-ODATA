



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DCQ6PGQ%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T061142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWzsv7T%2FulNFIQW1Yq6y2lPju4mPy8gEw8T9ROu5o1AiEA5T92I3fqrWH7K1aJ46eNTAN%2Be8MqogcyCYAkbZNWtXYq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDLX%2FS44PhVGcb6s%2BBSrcA9Dy%2BOJYWcnRTsCYWQ%2FZqlPM4N6sRtpQmPsXWkMy33z4BDgEli5qhSP3FArKtHoVmnvYl2ZqSdgOtDfYqmy%2Fgx1yib05NZpTXX3EftEMCFfMkbHF%2FNZJ2tmzaT3QCUjZ7Y3xpqbP2J8iZpgAq%2BbTwfIdf338uP5ktjOE7Kt%2FryOhBYlYiuE7CyhfAKsXdjYjnR29l40LTa1mdJsV7X1y5ooIpI76MV60u2PG0nx0ENnI1xr5sQbb0lsAeVnXRS1l97L0f4NDm5m%2BPgncdNB3KirNGdPg%2B%2BkciDqzd35gWlRUuWX4drMIXxagJsSTzrgItWekqBiTPWrX9WNepE4wMBf0RQNqR1X%2FBPzpBhJsRNp1p6l2VHuLmI%2BUUAZ%2BOrVlEsS57zr%2B9pCtw6p%2BPIE%2FCgvzG%2BXNDTyc5ww21eIio0N%2F8Rtuxa3Rbf9kD0T8eFUXJCJeeEtO%2F8aXja3OK5unbg29o2C1FJzPFkqmpFOdPIaxfhz3QAy9CEXwlJu4MdCU0H9ku8LkCo%2FkO0BvHhj9RUVZ9k%2BOieQffE%2FU946mk2V5ftChzUNUFZYEPXmdTS859mSpkJqo8MRtwVTPm2cZnII%2BmqpjI0RsJzqNx9Awg99p33XiqV%2BtcAZszvrgML3YvNUGOqUB0OYiZopNDxMXml3Jv0LTGS8UzFiADoUass6W3%2Fpe0gqt40LF0nmMJszeUUV92vs0sJkoIUpe2z456%2F2iUFB80S%2Fzu%2BcRc4shXsW4jk26HI6LQVs05ZGVk1wVY12DZGUW2kxxgIgonM0tbwxowB06So7XBHjso0DvYbD92tJZ7DjBj1z00mjFTKwJ7fWeBXeBGaIAnjal3mm2Qv4e1bucu%2F1rCPZ6&X-Amz-Signature=d3334c6cd9c20fbaf7e2b698a224ccd3792c350462761d7bf58f83959783e824&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DCQ6PGQ%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T061142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFuWzsv7T%2FulNFIQW1Yq6y2lPju4mPy8gEw8T9ROu5o1AiEA5T92I3fqrWH7K1aJ46eNTAN%2Be8MqogcyCYAkbZNWtXYq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDLX%2FS44PhVGcb6s%2BBSrcA9Dy%2BOJYWcnRTsCYWQ%2FZqlPM4N6sRtpQmPsXWkMy33z4BDgEli5qhSP3FArKtHoVmnvYl2ZqSdgOtDfYqmy%2Fgx1yib05NZpTXX3EftEMCFfMkbHF%2FNZJ2tmzaT3QCUjZ7Y3xpqbP2J8iZpgAq%2BbTwfIdf338uP5ktjOE7Kt%2FryOhBYlYiuE7CyhfAKsXdjYjnR29l40LTa1mdJsV7X1y5ooIpI76MV60u2PG0nx0ENnI1xr5sQbb0lsAeVnXRS1l97L0f4NDm5m%2BPgncdNB3KirNGdPg%2B%2BkciDqzd35gWlRUuWX4drMIXxagJsSTzrgItWekqBiTPWrX9WNepE4wMBf0RQNqR1X%2FBPzpBhJsRNp1p6l2VHuLmI%2BUUAZ%2BOrVlEsS57zr%2B9pCtw6p%2BPIE%2FCgvzG%2BXNDTyc5ww21eIio0N%2F8Rtuxa3Rbf9kD0T8eFUXJCJeeEtO%2F8aXja3OK5unbg29o2C1FJzPFkqmpFOdPIaxfhz3QAy9CEXwlJu4MdCU0H9ku8LkCo%2FkO0BvHhj9RUVZ9k%2BOieQffE%2FU946mk2V5ftChzUNUFZYEPXmdTS859mSpkJqo8MRtwVTPm2cZnII%2BmqpjI0RsJzqNx9Awg99p33XiqV%2BtcAZszvrgML3YvNUGOqUB0OYiZopNDxMXml3Jv0LTGS8UzFiADoUass6W3%2Fpe0gqt40LF0nmMJszeUUV92vs0sJkoIUpe2z456%2F2iUFB80S%2Fzu%2BcRc4shXsW4jk26HI6LQVs05ZGVk1wVY12DZGUW2kxxgIgonM0tbwxowB06So7XBHjso0DvYbD92tJZ7DjBj1z00mjFTKwJ7fWeBXeBGaIAnjal3mm2Qv4e1bucu%2F1rCPZ6&X-Amz-Signature=c157c1c14fbafb677d8cd552519f862d3f42d703620efdabda9b8959382ea4ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







