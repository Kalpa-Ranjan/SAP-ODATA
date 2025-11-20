



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDAQT6YI%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T062248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBmk9KCTEldhWNPEe0WUUFx7EsDYLVpEF19bOM3eXpZpAiEAqLYvM7ez0%2BNlx5cP%2Fvvgm%2B%2Bwt4pI7ytLmIKz0ttyonAqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNanQksgfsUF4sHL6SrcAxZg7HBnJwYqZ52THQnzrlHKUOzR5UwBgjhHcXPqXJ6OMEchlrJ4mImRJwpyFCLHD2l41AafD9xHKZQ22KvSV6y6ZCg47ENlgU1dQktRwqpDNd6ZMV%2By%2FWiwmdOBML1cNyDtzPDe2%2BToZZwisvbMwEdEzdO9MFnN4xC8esP7F7g8Ab4vXtLkI%2Fo1WDT6MGLxEnz4B0UqIutxrPzout1XfuNqN7xyy5I9rk%2BlH9mDBYrLWbal%2FXhsaERnTU%2BRDVa3jnH%2F3Bh1u1o1s2LtcJY6l032aD%2F2uZqns0sSjJJjdfNyo8xzLAbDhEhpLbHlKLfDXPBHzUpwZY0yFln6SDyp%2FSo%2FxxDRaxquS5iGW5kHJY4tnGOVhxzQ21%2FTBaexW1FLP2AIYWFiiJ7AFJkPa9JwxSXXnZM8SpvCICy7CkVvxz4tmj1O2l2Q8iGAeCjkUQAv9TB%2BDJVP0fI%2F%2FcK58Hl5r%2FcULfTK29tJMgf%2BHjB9gYhvAQMH7ALdIu%2B66mBUyaYJSX4Y1oTmoNJt7cDCTUV%2BKZX8n8vHWXTKqwSneoYlgQeghg2ywoWtUxWTmdSIdcnruKq4JxuvkopcsoPhQjRYQf47vnmnDWRmqODx2IkmO%2FGiVPQ71OQ%2Bry5CB7ptMIvP%2BsgGOqUBXaxDwAVG6E2HkBJXLW525pVzO2%2BY%2Bym4hPPn9IvGVpqMegMIUly5izT0Sl943QffyGxHCl%2FiTWWIt4BhYqn24frQxPn7Z5tvc2h%2B2OiSCYi%2FZWicBNcR7soLNpW%2FP2CTCLionaNKZJz7%2FZvKuW5gsDkAAXWOKMShw%2B%2Bc2GxLQ%2Fxe5dWk%2FPMsC8BNEj6wvHdpT69sOLaqlnO3JdTICjJD7r1u7v6q&X-Amz-Signature=2c7f6edd8aa32f65a3239ebb99570b813c6a4a0c0f5b8b59c79ec0425dca55ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDAQT6YI%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T062248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIBmk9KCTEldhWNPEe0WUUFx7EsDYLVpEF19bOM3eXpZpAiEAqLYvM7ez0%2BNlx5cP%2Fvvgm%2B%2Bwt4pI7ytLmIKz0ttyonAqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNanQksgfsUF4sHL6SrcAxZg7HBnJwYqZ52THQnzrlHKUOzR5UwBgjhHcXPqXJ6OMEchlrJ4mImRJwpyFCLHD2l41AafD9xHKZQ22KvSV6y6ZCg47ENlgU1dQktRwqpDNd6ZMV%2By%2FWiwmdOBML1cNyDtzPDe2%2BToZZwisvbMwEdEzdO9MFnN4xC8esP7F7g8Ab4vXtLkI%2Fo1WDT6MGLxEnz4B0UqIutxrPzout1XfuNqN7xyy5I9rk%2BlH9mDBYrLWbal%2FXhsaERnTU%2BRDVa3jnH%2F3Bh1u1o1s2LtcJY6l032aD%2F2uZqns0sSjJJjdfNyo8xzLAbDhEhpLbHlKLfDXPBHzUpwZY0yFln6SDyp%2FSo%2FxxDRaxquS5iGW5kHJY4tnGOVhxzQ21%2FTBaexW1FLP2AIYWFiiJ7AFJkPa9JwxSXXnZM8SpvCICy7CkVvxz4tmj1O2l2Q8iGAeCjkUQAv9TB%2BDJVP0fI%2F%2FcK58Hl5r%2FcULfTK29tJMgf%2BHjB9gYhvAQMH7ALdIu%2B66mBUyaYJSX4Y1oTmoNJt7cDCTUV%2BKZX8n8vHWXTKqwSneoYlgQeghg2ywoWtUxWTmdSIdcnruKq4JxuvkopcsoPhQjRYQf47vnmnDWRmqODx2IkmO%2FGiVPQ71OQ%2Bry5CB7ptMIvP%2BsgGOqUBXaxDwAVG6E2HkBJXLW525pVzO2%2BY%2Bym4hPPn9IvGVpqMegMIUly5izT0Sl943QffyGxHCl%2FiTWWIt4BhYqn24frQxPn7Z5tvc2h%2B2OiSCYi%2FZWicBNcR7soLNpW%2FP2CTCLionaNKZJz7%2FZvKuW5gsDkAAXWOKMShw%2B%2Bc2GxLQ%2Fxe5dWk%2FPMsC8BNEj6wvHdpT69sOLaqlnO3JdTICjJD7r1u7v6q&X-Amz-Signature=6475b224696eef9b07dc9378482fc499aa6414c3258bc3d4fd4fb8c6b4de518b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







