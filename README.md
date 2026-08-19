



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5CNQZR4%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T005527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrbT4cza64MrdZGnmxCTnQpIGdK8Zl5wxM%2B5WHD43v0wIhAPlrprW792bGojZLt2c%2FUhYToOBmO35MtzbEqJ6r0JG0Kv8DCGkQABoMNjM3NDIzMTgzODA1IgyxS2TJ4bMHgyNbxysq3AM5dMIuSqXuvUO0hCJogKSgOlsxIJemgWr7GqsbSeGS%2FcP8vMOxlAfsF%2F3wwkQ7zUK%2Fihpl1szf1W%2Buc%2F0DBpTq%2FRNaV3zlvLavAAsjm7fVk7wzX8elTQ6X1B%2Fbe3iZqBS0WUzEznWYxQiy4o7OkFZxC%2BtU2cXWlRMGwJ4nhQYmEHl%2F4QvJ0Ez76wENlgvj1sCUMKmfVCk%2Fgi2VAf5H5Q%2FPIpOhcXs8usnyojXK96BD8QPQS0ovCOf%2FETrWSjgP%2Fc%2Bqv43Rkz4K6b5XQuwXmLUomyEZ8UdM1pDY7nJ9fzGKFsEvB9cqA%2BVCjDLT4D5KDkBfO4mYSbBPmv%2BpwTb4U%2F3jSAk8Aru701f5%2BmIgqbD6IYAt6Oj0xIHVIKaw0Jh0%2FisN7dgH%2F%2BrfRMXfJGQfoaWFElRbyHTGlzmNlHKimFTp2rbZVOaOi7FjzrDi%2Fh3o2sTqNdaAPlDIkjGcpvcbb%2F%2BFRWGTaLcxlMDj2n4myjt%2FsPi49uTirTkzBhzi5zixUtXDzs%2Bc4J6fOFuSzRmiG21xZP5oHqQ3oOQvIti0C2tcD6MADE9%2Fpa0gAQPpE5Bg8kfILvE%2FN0Q3oMwQW3sirU3q3c%2F%2FR2NC8XK4mQh%2F%2Fnfv37fBFuD37HZOzQ%2BfBTCy4ZPUBjqkAdDySSnmNVVwLVYirYkCd8SWkB4trYdgOhimqpaAXZA%2F63bl6Kr%2F%2BO0HWi2pAJHmSQDAduhHdVD4dDz2WUNDJy5XiKy0%2F2ib89bUdZ6pyaYCUCkwuk%2Bi7wkDWDeu5yq1zQKTMDeyGoXYt2bXj37CJeNHUV0t3aVGnHJcYKrB1kCuKxFXECHOGuJaCHwOPT7rgB%2BEGK%2BUw5nNJF6U6L6LdH%2BoROUM&X-Amz-Signature=020671cb109d2ebd62b8b9c7c948a64e2971aa0d3084183d1f47195f10a98dde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5CNQZR4%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T005527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrbT4cza64MrdZGnmxCTnQpIGdK8Zl5wxM%2B5WHD43v0wIhAPlrprW792bGojZLt2c%2FUhYToOBmO35MtzbEqJ6r0JG0Kv8DCGkQABoMNjM3NDIzMTgzODA1IgyxS2TJ4bMHgyNbxysq3AM5dMIuSqXuvUO0hCJogKSgOlsxIJemgWr7GqsbSeGS%2FcP8vMOxlAfsF%2F3wwkQ7zUK%2Fihpl1szf1W%2Buc%2F0DBpTq%2FRNaV3zlvLavAAsjm7fVk7wzX8elTQ6X1B%2Fbe3iZqBS0WUzEznWYxQiy4o7OkFZxC%2BtU2cXWlRMGwJ4nhQYmEHl%2F4QvJ0Ez76wENlgvj1sCUMKmfVCk%2Fgi2VAf5H5Q%2FPIpOhcXs8usnyojXK96BD8QPQS0ovCOf%2FETrWSjgP%2Fc%2Bqv43Rkz4K6b5XQuwXmLUomyEZ8UdM1pDY7nJ9fzGKFsEvB9cqA%2BVCjDLT4D5KDkBfO4mYSbBPmv%2BpwTb4U%2F3jSAk8Aru701f5%2BmIgqbD6IYAt6Oj0xIHVIKaw0Jh0%2FisN7dgH%2F%2BrfRMXfJGQfoaWFElRbyHTGlzmNlHKimFTp2rbZVOaOi7FjzrDi%2Fh3o2sTqNdaAPlDIkjGcpvcbb%2F%2BFRWGTaLcxlMDj2n4myjt%2FsPi49uTirTkzBhzi5zixUtXDzs%2Bc4J6fOFuSzRmiG21xZP5oHqQ3oOQvIti0C2tcD6MADE9%2Fpa0gAQPpE5Bg8kfILvE%2FN0Q3oMwQW3sirU3q3c%2F%2FR2NC8XK4mQh%2F%2Fnfv37fBFuD37HZOzQ%2BfBTCy4ZPUBjqkAdDySSnmNVVwLVYirYkCd8SWkB4trYdgOhimqpaAXZA%2F63bl6Kr%2F%2BO0HWi2pAJHmSQDAduhHdVD4dDz2WUNDJy5XiKy0%2F2ib89bUdZ6pyaYCUCkwuk%2Bi7wkDWDeu5yq1zQKTMDeyGoXYt2bXj37CJeNHUV0t3aVGnHJcYKrB1kCuKxFXECHOGuJaCHwOPT7rgB%2BEGK%2BUw5nNJF6U6L6LdH%2BoROUM&X-Amz-Signature=ef1212f5cdc56d3259c579939247fa3c1c69e40b859162be6548fa46fe38e177&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







