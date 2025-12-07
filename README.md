



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZXQY6AB%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T182033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg7ywMn6jQS5kqgny7waV9Y1ok8zNZR2QiMo%2FucLnMEQIgXviZheGQavgR6Ah7VT9MRb8pbmNyWK1doZK80ADr5TMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQbtvE4ilHIzqBwBCrcAz2g4lM17V7kT4sgu334%2BDvdZnMZNd5N8am7qPel1p%2F%2FJn5VPO2h9sl6rKxXQ7QjXxXXGDIvX9ZGae67O2AhrjSLEBIx%2BHH%2BNVIKe4YDgOtLVBg7t%2Fu4JZ6BkkTOYV3WgPhv3GUfNEqrOmb9liA5tGSYqP4DCLrhp4%2BXJgUvqgm4k0Or9%2BLeP5lNGv%2FPyeyzyCCI9qXMP8jqbaX2yaQY48SA4Y0mzWJQpPhSBhC6Zil1ThQwIvYeHs3dsyBWXIYzSQCOq9w01enLELdHCUzxvAWgFnN%2FJzbPR%2FwVl0hba%2FIa1dXO%2F0lpVc2ELS7c5qT1NYLw4r6mOE0FSQF77JbHUq0biS8w6Vl8uT6WzJPuEnjOoUclkCvihbvSDaLMlg0SMnGVuAKRStyjXAudOBz3wrwt276diY2hS1Ugz%2BVidIttt6B1eHEO5N2FnlWyRE4jHs4w39ePMRDklcARKsYuKsWigzpL%2BNeHEII2Pbb%2BQ1pXDeAQxAuWmvbLyba3NKD8NRNp8jaUaujBpXXFdR4dthiOFgl3s8%2Bc6pKozuGU%2BWIdRCcR8hsge16TGu3DyeLiZI1zq6H8P7WLdgATlCwhLMZ7TrNxBCWZp49J5K5YpTsMnUe1mQg%2BPvRH0LMPMJq11skGOqUBnimlmqDxeUIt6i79xOuKof5BNdO80JYmDpL4fDocUxPn7vd0%2F7iWV%2Flnerr72bIIKGw3IyvScSikN9vuKUOl5IGUOyFEuxVW6F4HvBQDIK8j7nJKuD04HXAvcXmqQ30toJedr%2FK3i%2FuQ0i8l%2BKla%2B62yedcPQxwwduUQnoWdZv5kLPx6xOb60yppx2NXph5iEDXulfkCHWHGUGrnB5iR3U6I%2FIEn&X-Amz-Signature=861c0d33f1040fee13f8c2fe7dfa98a951b10eca5bc4c08d5a47d86331e6af49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZXQY6AB%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T182033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCg7ywMn6jQS5kqgny7waV9Y1ok8zNZR2QiMo%2FucLnMEQIgXviZheGQavgR6Ah7VT9MRb8pbmNyWK1doZK80ADr5TMqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQbtvE4ilHIzqBwBCrcAz2g4lM17V7kT4sgu334%2BDvdZnMZNd5N8am7qPel1p%2F%2FJn5VPO2h9sl6rKxXQ7QjXxXXGDIvX9ZGae67O2AhrjSLEBIx%2BHH%2BNVIKe4YDgOtLVBg7t%2Fu4JZ6BkkTOYV3WgPhv3GUfNEqrOmb9liA5tGSYqP4DCLrhp4%2BXJgUvqgm4k0Or9%2BLeP5lNGv%2FPyeyzyCCI9qXMP8jqbaX2yaQY48SA4Y0mzWJQpPhSBhC6Zil1ThQwIvYeHs3dsyBWXIYzSQCOq9w01enLELdHCUzxvAWgFnN%2FJzbPR%2FwVl0hba%2FIa1dXO%2F0lpVc2ELS7c5qT1NYLw4r6mOE0FSQF77JbHUq0biS8w6Vl8uT6WzJPuEnjOoUclkCvihbvSDaLMlg0SMnGVuAKRStyjXAudOBz3wrwt276diY2hS1Ugz%2BVidIttt6B1eHEO5N2FnlWyRE4jHs4w39ePMRDklcARKsYuKsWigzpL%2BNeHEII2Pbb%2BQ1pXDeAQxAuWmvbLyba3NKD8NRNp8jaUaujBpXXFdR4dthiOFgl3s8%2Bc6pKozuGU%2BWIdRCcR8hsge16TGu3DyeLiZI1zq6H8P7WLdgATlCwhLMZ7TrNxBCWZp49J5K5YpTsMnUe1mQg%2BPvRH0LMPMJq11skGOqUBnimlmqDxeUIt6i79xOuKof5BNdO80JYmDpL4fDocUxPn7vd0%2F7iWV%2Flnerr72bIIKGw3IyvScSikN9vuKUOl5IGUOyFEuxVW6F4HvBQDIK8j7nJKuD04HXAvcXmqQ30toJedr%2FK3i%2FuQ0i8l%2BKla%2B62yedcPQxwwduUQnoWdZv5kLPx6xOb60yppx2NXph5iEDXulfkCHWHGUGrnB5iR3U6I%2FIEn&X-Amz-Signature=4027906f6aba2687d1ea809c95f5288ab17b94ad55f56965a3f6b368ec6d8666&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







