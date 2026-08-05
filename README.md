



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VICUIX6J%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T082656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDbdEswHZ%2F3NFSqRh4vh9le5wZu2qxpy1Vh23lzL47JHwIhAKtaBFyItxRFnQhGo7Ad3HbFKBNNejYg47fUN1z3hCTFKv8DCCEQABoMNjM3NDIzMTgzODA1IgyRtT1GLfO8zXevHEMq3ANhnO58T%2FbhjTp7BDBTOsFy4BVQXdI8U0MB7vgkiLHNPDyhZ6sDPf0Rad%2B9eShcBYNJ5mSo2buNAcCZoeGtA60TaJQCsR37T%2BEsrgD4wLkmSQScGgBNMJpk%2BbUxphe%2Bf44yK89kW%2FKZS8E%2F3vCkj5bvRihpNt1M4fJUm0Hc0oUkkal2%2BjQiChtPYSHVWSPriyCJ2lhrt%2FIng41AFq6crSIQfbKA2hfPbWBWIxNfHmb1U6zCSiaJtygmYH%2B%2F%2FDvlcya52%2Bv6VT9pJx6qG65tcVfGuvN9MtrjrgjuC8AO6mDE2CrkBEqPM86yz7gZy8BGw0qgyhs%2FzUTcqhDO6pOpVyotVmvNFOWWH1779bFnY22CvgXWi0roVXqWE9REKk%2FUE84XeA1V3nKP6nB6804elXo2aasY0AZKoDNOXFOJ9JgRiG7A%2FC8V9ojSDZr9PYnFtlZvK3XH%2BtH8QjDY0JifEJQkofhAZyLfRadww4%2Bwi7T9xqKMWOzK2EYYlxr8zecz%2FzokwPofEZ4Oc%2F7bGJY50fycosNv%2BUlHSF5ulmv%2BtVRitUn24czGJdD7%2FysmmjMHkfPKvXQk0BDWiakl6elGwGMG5%2FRVHbEMHxpShEeftrcAEhXUmy3mfv0JOvBfYjDx28vTBjqkAeWJXhw1N98wxBif9BQ4B0EIzsaoxT4quD4ZsN1ZNn9KSWxz0Dy0MfEeRtnRx8TH2fft0fk%2BMpBOQo3es%2BYV8gzDWS1R5VWrTFH6zUr7T8tMOBA9kvkvlmO2Cr0iPQuoLzzq2WjhJ%2Bubt%2BBwIQ2QHR7MeOPK22N%2B0uGV2qnABdk7JkZvUmRIBGKXfGnQ1oviTMAg7D%2FCC8%2B3u%2BLB9XAX%2B95K%2FZxa&X-Amz-Signature=988eabdadb0006b8a532fc11e36877cc9a57c0cb3778f03a4da63a7b7ddff3e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VICUIX6J%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T082656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQDbdEswHZ%2F3NFSqRh4vh9le5wZu2qxpy1Vh23lzL47JHwIhAKtaBFyItxRFnQhGo7Ad3HbFKBNNejYg47fUN1z3hCTFKv8DCCEQABoMNjM3NDIzMTgzODA1IgyRtT1GLfO8zXevHEMq3ANhnO58T%2FbhjTp7BDBTOsFy4BVQXdI8U0MB7vgkiLHNPDyhZ6sDPf0Rad%2B9eShcBYNJ5mSo2buNAcCZoeGtA60TaJQCsR37T%2BEsrgD4wLkmSQScGgBNMJpk%2BbUxphe%2Bf44yK89kW%2FKZS8E%2F3vCkj5bvRihpNt1M4fJUm0Hc0oUkkal2%2BjQiChtPYSHVWSPriyCJ2lhrt%2FIng41AFq6crSIQfbKA2hfPbWBWIxNfHmb1U6zCSiaJtygmYH%2B%2F%2FDvlcya52%2Bv6VT9pJx6qG65tcVfGuvN9MtrjrgjuC8AO6mDE2CrkBEqPM86yz7gZy8BGw0qgyhs%2FzUTcqhDO6pOpVyotVmvNFOWWH1779bFnY22CvgXWi0roVXqWE9REKk%2FUE84XeA1V3nKP6nB6804elXo2aasY0AZKoDNOXFOJ9JgRiG7A%2FC8V9ojSDZr9PYnFtlZvK3XH%2BtH8QjDY0JifEJQkofhAZyLfRadww4%2Bwi7T9xqKMWOzK2EYYlxr8zecz%2FzokwPofEZ4Oc%2F7bGJY50fycosNv%2BUlHSF5ulmv%2BtVRitUn24czGJdD7%2FysmmjMHkfPKvXQk0BDWiakl6elGwGMG5%2FRVHbEMHxpShEeftrcAEhXUmy3mfv0JOvBfYjDx28vTBjqkAeWJXhw1N98wxBif9BQ4B0EIzsaoxT4quD4ZsN1ZNn9KSWxz0Dy0MfEeRtnRx8TH2fft0fk%2BMpBOQo3es%2BYV8gzDWS1R5VWrTFH6zUr7T8tMOBA9kvkvlmO2Cr0iPQuoLzzq2WjhJ%2Bubt%2BBwIQ2QHR7MeOPK22N%2B0uGV2qnABdk7JkZvUmRIBGKXfGnQ1oviTMAg7D%2FCC8%2B3u%2BLB9XAX%2B95K%2FZxa&X-Amz-Signature=82584e4823dfdac2c9503f7b364806b884052319a808eebb2d2615001c6dbee8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







