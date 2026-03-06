



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNHXRIDW%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T014649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCCrKHtugCsn4MiC97nc2VcktoqNo4HN%2FLly5SpVG3kFAIgCc1DZJp%2BoggB%2B6%2FFI0%2BEKthD5gYiaGB2hFNH0ulM8ygqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZqIJmys3PSxkNW2ircA7DaSt1bIyFnI0vcdxQip9vJdX8nGmaW%2BbbihvHBRqEsopxbrU4ejRgdb6dtbkmEUKHfqVu2kFWORnC3vJpdM%2FTfuepLYVAokO3bYFgHukwOeE1FL6RzQ9roDZl1gUXasBqwD2Ln9ynxawzEvgrxI8yEjU6rJ4j5TtGBjOAtG%2BX%2FL5EfreKKEoZ%2BeFgT5880F1lfR%2F6cpBOdIQ4obRHTUFoNy07syZA7oXIqD8qz3PK24oBcLIGPv5FIgxbHoGmRvAHKOPA0B18LM%2FTCdMwkBLu1OFbGYJeb0FOt6YXZ9w66hnkYEO7U351W1hvgzySY5HECG%2BOG1HjzETSrO9MOErkhVVWTpm2Psfh3%2B7A6QIeruX5RGLaXJMBfEanSM5oGstId%2B%2Bph1bMiwspgS5bWxvuv2YP%2BsoVbH7O36sF6%2B8gzlL2rImY7ESm7Q%2B6Qjh9Q96Arvna8A93RjtA2YHX00YnS2rsKqG6n5MQ2WXOpZgr9Tc7vnHLjxUt%2BmRV%2BSpYEhcWumn%2FFPgobbe3GcITEdx3P%2Fjvz48WLuRmWo0D4sVKC4KPqWat7tjGLxU2cLwaZmHs0zcQRwQMOYZTzTsQrnALGOS3ntKxn3ElZVImQGLJDEW50sMMZFcTVchWKMMvPqM0GOqUBQhEb5wYxVYx%2FcnoVZr9Q6c8raiOV29UfiesfudwPFW%2BkwJwMiimtnoJ0myE%2F3eB5ndVeNjowrrVJN%2BIENs3Lx9HjiKisxI3OUpcqICwSc%2BCFo8MO3sgcBGXNUajM7fj5ixrZqXEXnhSEJc%2Bh8XbKQiKm3rYjD0FjxZXcx82%2BodePYR2QRca%2FFyhbjUnNAkpkBo0UmHLacFIurZXekGyDK5xmBGmQ&X-Amz-Signature=79f074eeedeb2853e780befac48e4e2c11a4c5cb34e9f82961d2ffc292dd08db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNHXRIDW%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T014649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCCrKHtugCsn4MiC97nc2VcktoqNo4HN%2FLly5SpVG3kFAIgCc1DZJp%2BoggB%2B6%2FFI0%2BEKthD5gYiaGB2hFNH0ulM8ygqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZqIJmys3PSxkNW2ircA7DaSt1bIyFnI0vcdxQip9vJdX8nGmaW%2BbbihvHBRqEsopxbrU4ejRgdb6dtbkmEUKHfqVu2kFWORnC3vJpdM%2FTfuepLYVAokO3bYFgHukwOeE1FL6RzQ9roDZl1gUXasBqwD2Ln9ynxawzEvgrxI8yEjU6rJ4j5TtGBjOAtG%2BX%2FL5EfreKKEoZ%2BeFgT5880F1lfR%2F6cpBOdIQ4obRHTUFoNy07syZA7oXIqD8qz3PK24oBcLIGPv5FIgxbHoGmRvAHKOPA0B18LM%2FTCdMwkBLu1OFbGYJeb0FOt6YXZ9w66hnkYEO7U351W1hvgzySY5HECG%2BOG1HjzETSrO9MOErkhVVWTpm2Psfh3%2B7A6QIeruX5RGLaXJMBfEanSM5oGstId%2B%2Bph1bMiwspgS5bWxvuv2YP%2BsoVbH7O36sF6%2B8gzlL2rImY7ESm7Q%2B6Qjh9Q96Arvna8A93RjtA2YHX00YnS2rsKqG6n5MQ2WXOpZgr9Tc7vnHLjxUt%2BmRV%2BSpYEhcWumn%2FFPgobbe3GcITEdx3P%2Fjvz48WLuRmWo0D4sVKC4KPqWat7tjGLxU2cLwaZmHs0zcQRwQMOYZTzTsQrnALGOS3ntKxn3ElZVImQGLJDEW50sMMZFcTVchWKMMvPqM0GOqUBQhEb5wYxVYx%2FcnoVZr9Q6c8raiOV29UfiesfudwPFW%2BkwJwMiimtnoJ0myE%2F3eB5ndVeNjowrrVJN%2BIENs3Lx9HjiKisxI3OUpcqICwSc%2BCFo8MO3sgcBGXNUajM7fj5ixrZqXEXnhSEJc%2Bh8XbKQiKm3rYjD0FjxZXcx82%2BodePYR2QRca%2FFyhbjUnNAkpkBo0UmHLacFIurZXekGyDK5xmBGmQ&X-Amz-Signature=6a3f6d3589324dae351d95a18a0aa5657e0ab9dca7778ee257b22f0b7c66e617&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







