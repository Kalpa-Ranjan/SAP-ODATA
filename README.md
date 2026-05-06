



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKFDPE4T%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T135554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcmJgLH8IvIKkENtWvnNEWbELwtv%2FBhEOo2A1seKOmAAIgY8bk9GMgFi3bjHtjroYnOxDerZzHcIpy%2BckKf4faQawqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj6zWwZCBaggX0Q0ircAzPCFmIXnXG8HSxGaDjoJ%2FowKKCpI%2Fx6WGfELJ%2F4xOowag0us%2F17UExAzEkh9h%2FeePqWSF1SO0B4zddqacFBRrGYurLtCGJf1gvMDt%2B4n1WJz6gE3IkOOhNAMSvUC60nNOmrMdTN46LUZoCfwo5nHOpLnDtGkemD0w7hugP%2F2tE%2F3mn6u9p5S7U5JpNHpgHx3OV342JPgIH4xMgwLLFKfqNpd%2BkiDuId38jzE8ntfjKwcNlsVFG4A1ej4yAZIomkoRcRD%2B1jFbD8fO%2Bym3ZP%2B6Qtd8hWJAlaLDbsh%2Fj7LFf0bv8988znsVFVTE2aAdEWD7xZTBcIg%2Bag%2F%2BVIiJ9hYa5Nvn4LAKDnA6gz74Se07zTkWQt3hoZSAaDRFlhiu%2FZs6Ng%2BkrNcSYhfZGtasR0LGLQBP6IfXsv0N9rPAfF7nTSBu60v%2FVyZKJtR5XknZ36KwfjAJk88nSfANtiIy%2F8%2BiLr2%2FrNjrS7364EFznWvEMEgB0xW0WYjjWBoTZCsuwfrl1D209wVBf7v%2B4tgtM4KbVW6BGBE%2F7kV21rAiCckdRRPqi4LH8RTA7f%2FYJMAYFEIqvAaeAAeasPkwYyCMKHPPOYcUKskgLTbc%2BPJDhQu5QXrFewUFzDG59OpkRLMJ6J7c8GOqUBJXkEEjawGRWmeu1xDG8CXuLRud8emLh1FwYF8v5znGQXiPaDhSbP4ywWownvRTzEzzuA4vOdkVuCo0dyOwHGEOXprcDHeJNnqin8xB09k3%2FNS7tiPsQAru6Q1JoM%2Bhw1GEkHQQrfJL6cc0Olg0vgERbNj0QKxzFdII01YawuLFWfHpLkvf3GFgx8UTxYOvenfif0q4HwFKiUciOW72MkmIqMXFHo&X-Amz-Signature=c4503f398d0663ce61fff87e1525ec67ee454e62648f94bb31d26809ec9bed33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKFDPE4T%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T135554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcmJgLH8IvIKkENtWvnNEWbELwtv%2FBhEOo2A1seKOmAAIgY8bk9GMgFi3bjHtjroYnOxDerZzHcIpy%2BckKf4faQawqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEj6zWwZCBaggX0Q0ircAzPCFmIXnXG8HSxGaDjoJ%2FowKKCpI%2Fx6WGfELJ%2F4xOowag0us%2F17UExAzEkh9h%2FeePqWSF1SO0B4zddqacFBRrGYurLtCGJf1gvMDt%2B4n1WJz6gE3IkOOhNAMSvUC60nNOmrMdTN46LUZoCfwo5nHOpLnDtGkemD0w7hugP%2F2tE%2F3mn6u9p5S7U5JpNHpgHx3OV342JPgIH4xMgwLLFKfqNpd%2BkiDuId38jzE8ntfjKwcNlsVFG4A1ej4yAZIomkoRcRD%2B1jFbD8fO%2Bym3ZP%2B6Qtd8hWJAlaLDbsh%2Fj7LFf0bv8988znsVFVTE2aAdEWD7xZTBcIg%2Bag%2F%2BVIiJ9hYa5Nvn4LAKDnA6gz74Se07zTkWQt3hoZSAaDRFlhiu%2FZs6Ng%2BkrNcSYhfZGtasR0LGLQBP6IfXsv0N9rPAfF7nTSBu60v%2FVyZKJtR5XknZ36KwfjAJk88nSfANtiIy%2F8%2BiLr2%2FrNjrS7364EFznWvEMEgB0xW0WYjjWBoTZCsuwfrl1D209wVBf7v%2B4tgtM4KbVW6BGBE%2F7kV21rAiCckdRRPqi4LH8RTA7f%2FYJMAYFEIqvAaeAAeasPkwYyCMKHPPOYcUKskgLTbc%2BPJDhQu5QXrFewUFzDG59OpkRLMJ6J7c8GOqUBJXkEEjawGRWmeu1xDG8CXuLRud8emLh1FwYF8v5znGQXiPaDhSbP4ywWownvRTzEzzuA4vOdkVuCo0dyOwHGEOXprcDHeJNnqin8xB09k3%2FNS7tiPsQAru6Q1JoM%2Bhw1GEkHQQrfJL6cc0Olg0vgERbNj0QKxzFdII01YawuLFWfHpLkvf3GFgx8UTxYOvenfif0q4HwFKiUciOW72MkmIqMXFHo&X-Amz-Signature=edd675111918fbf9e1545af528bbff51e9928b8a3f9b4ae437708d1f9549e468&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







