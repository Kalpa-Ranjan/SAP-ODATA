



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZXIKZ7K%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T061311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChGkEWU%2BcXSQ0bGNLTg8Qy%2BduAJTZJTbMnL7dcShcnXwIgKUgCWUKOEPXRB5T9%2F2%2Fe%2FnH2nS36JjLjOC6ObEZMdiIq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDElHWNm%2BcBfJMLx4wCrcAxp6mZgQ4%2F7%2FLPPwFpAPd2gKIPKEZNf%2BCG2BG3XSZ%2B3CXskM%2FwsdVF7fJl%2FPTkpiKMEPW%2B6wzZsuclfXDyFArRTPqN%2BD3NmE9vKP9NdePB4cs0cJiuBosKswEyTqe7PwcnRgnHfdW1h1jHzBH0z%2BAEfS%2B8RBocR3hQ4FySe0cC3yKYCl8wMqY1Z%2FFlPDnTZ6hGmTlurvVwBXAJ%2BymFnUY%2FFrYsir6ZYUWdPchPOHJwuFO%2FpOyJTnkxvGsB1pZzXqqqQhh2D%2Fe0aZGYo1ajH5kYQjCQy5GrgjOGzOGzcYlaJDMQWZt6CaFzMYqCD5q%2B1%2F4DzAy8MGNASCmMioaBWZegaaFFx1NcIQ031T6bliSvHlasSGz5fqQ3jGuNY6iQKeY6veObciUczXLAOo7eACSNmIOuN3wQIUWWsxDYGZ%2FIZlW6vu%2B3eiar0E7WBnEUn07S0VA0ytHxrJpfGhDxywpmfHKog1FuAqfpu7HfO5cgkO4h1it0aQRCUBEhYa72mKi6VASGJFgrsu%2BnBFIG8%2BRiEsGGvE%2F5pFo8F%2B2qOSZ0iro%2FcNdMvKn%2Fbd1ddFyQLgfKfWth9VvW%2BuI0twjmGR1dT8uW%2FfV8HAcqOua6TNaPXNXG3ivjNm%2BIBS5RCTMJn7ltYGOqUBQKWpes9w7LSwJqETx521qa06S4gYnL9x4fc9iGTSZ4%2FyzY6SqYYpqfYhZ68CO3iTR%2F%2BKGt4MRYrqyP9qIpKlRc%2B3AmKgMCrLbCwIcuTnRmWxh6ItJI2gYGHlxqKNs%2FLOLqT8bG87bCfEnOp9Cf2tsoRrT8Ow2Rdy56rkpc6cHrVrFFAqilp23oC2VdCBlBlcYaAL6d564LilyrKjNy787hUE1ejj&X-Amz-Signature=f2221512b7565f0400196a8b02279e9cb4a2ac680f49398222377bc4717139a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZXIKZ7K%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T061311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQChGkEWU%2BcXSQ0bGNLTg8Qy%2BduAJTZJTbMnL7dcShcnXwIgKUgCWUKOEPXRB5T9%2F2%2Fe%2FnH2nS36JjLjOC6ObEZMdiIq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDElHWNm%2BcBfJMLx4wCrcAxp6mZgQ4%2F7%2FLPPwFpAPd2gKIPKEZNf%2BCG2BG3XSZ%2B3CXskM%2FwsdVF7fJl%2FPTkpiKMEPW%2B6wzZsuclfXDyFArRTPqN%2BD3NmE9vKP9NdePB4cs0cJiuBosKswEyTqe7PwcnRgnHfdW1h1jHzBH0z%2BAEfS%2B8RBocR3hQ4FySe0cC3yKYCl8wMqY1Z%2FFlPDnTZ6hGmTlurvVwBXAJ%2BymFnUY%2FFrYsir6ZYUWdPchPOHJwuFO%2FpOyJTnkxvGsB1pZzXqqqQhh2D%2Fe0aZGYo1ajH5kYQjCQy5GrgjOGzOGzcYlaJDMQWZt6CaFzMYqCD5q%2B1%2F4DzAy8MGNASCmMioaBWZegaaFFx1NcIQ031T6bliSvHlasSGz5fqQ3jGuNY6iQKeY6veObciUczXLAOo7eACSNmIOuN3wQIUWWsxDYGZ%2FIZlW6vu%2B3eiar0E7WBnEUn07S0VA0ytHxrJpfGhDxywpmfHKog1FuAqfpu7HfO5cgkO4h1it0aQRCUBEhYa72mKi6VASGJFgrsu%2BnBFIG8%2BRiEsGGvE%2F5pFo8F%2B2qOSZ0iro%2FcNdMvKn%2Fbd1ddFyQLgfKfWth9VvW%2BuI0twjmGR1dT8uW%2FfV8HAcqOua6TNaPXNXG3ivjNm%2BIBS5RCTMJn7ltYGOqUBQKWpes9w7LSwJqETx521qa06S4gYnL9x4fc9iGTSZ4%2FyzY6SqYYpqfYhZ68CO3iTR%2F%2BKGt4MRYrqyP9qIpKlRc%2B3AmKgMCrLbCwIcuTnRmWxh6ItJI2gYGHlxqKNs%2FLOLqT8bG87bCfEnOp9Cf2tsoRrT8Ow2Rdy56rkpc6cHrVrFFAqilp23oC2VdCBlBlcYaAL6d564LilyrKjNy787hUE1ejj&X-Amz-Signature=69ab204d1af637584e1da7af5702cd40c7bc2c1db9959c18366ce383e1338ca4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







