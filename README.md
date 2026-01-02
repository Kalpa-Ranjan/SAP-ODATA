



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WY7NOJGL%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T182350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIApydGTZqOVe6kpDlfXtfAq0Aod7CAgVoR%2B004E0tbRTAiB1sfmLzAMGbLmepen9K6OJa%2BJo%2FnHH%2BGQusBDHTdK9Cyr%2FAwgAEAAaDDYzNzQyMzE4MzgwNSIMa1vVwq6FN7G0VA2qKtwDuHzYb%2FSpDzIV9rVeGBj%2Fz2%2FiBsphzLQ5RjvssglWOMUWGoZhGf6pHqUoy5nuCkRAH3n%2FSjtn4SyWl%2B4ss89p3Wr%2F509OX1OEunny4Fx%2FP9gSYZXUCxF0%2BV2%2Fl3eX0peVEbfa2qhSHWBE8UMeAq4bwjTyvpJcFOjnc4WtdXDWf%2Fk5ro6HKH8V%2FA050hYDnJ97KWdYw8%2BNhrSoJcgukHPKUB6%2FinRuNz9x1HMumci27PCSI8GEF59e3U7Ku2AFonGqoPHSF4CPNupJ7pv%2Fx9J%2F3QqqqwM5eet26dxeHIDLp4dVhAlkvlkfvoc6ZOP2LBPwsvtb%2BE0dcsMD6vQGF%2ByXsqpgJ0Nc%2BhxQU1ROwnYEPOMMFA94x%2FwTzVmEV3VqxSLsXtn14BwrBllWqPng8P%2FuqPeR%2BD%2Bt6AbmqBHL7B4oUxirh%2Bi6wAjvxZNTEmnPfFKm8EceLnFvo0kHB77kpygjbzPPSiiJc7gI4Hwe%2BK05RD9hCn1p1LDdPridZYIxxrZe1%2BW6gCP%2BBaMFejZDw1FoFIeXiiQhsOVcYc5cOpQrh8QWQWauN31rsEgs%2FNifY%2Fl1ULCUbdmPMiRC36PaXb9jV0sOMYGwSS7vaxCf5%2BY9rqY8xHmg2e88QSIxNuMwx6zfygY6pgGWLQBBKzCuo9Jd6a8lSn%2F59ja519xHy7aRAojdZHRUrIHcHiRd4N11dSyLorRS8u9kR01fRlOgSBztfe0bCjfNX%2FlM9bDvc%2FqCQBmed4UccOdeDovod%2BvG1xC9lo7qHFI%2F97AoarzZ6wM3nH7VMpQYEVqboEeaCc84D1aHARwEQ9vKuv4Cj07uiSGu3ehdX2r0HimQ32Sp6q9yJPt%2FqwjdW2AuxGrI&X-Amz-Signature=9b9f52b2318efeb48a8ad9a13c43259e271598697a08704060d33240abca214e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WY7NOJGL%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T182350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIApydGTZqOVe6kpDlfXtfAq0Aod7CAgVoR%2B004E0tbRTAiB1sfmLzAMGbLmepen9K6OJa%2BJo%2FnHH%2BGQusBDHTdK9Cyr%2FAwgAEAAaDDYzNzQyMzE4MzgwNSIMa1vVwq6FN7G0VA2qKtwDuHzYb%2FSpDzIV9rVeGBj%2Fz2%2FiBsphzLQ5RjvssglWOMUWGoZhGf6pHqUoy5nuCkRAH3n%2FSjtn4SyWl%2B4ss89p3Wr%2F509OX1OEunny4Fx%2FP9gSYZXUCxF0%2BV2%2Fl3eX0peVEbfa2qhSHWBE8UMeAq4bwjTyvpJcFOjnc4WtdXDWf%2Fk5ro6HKH8V%2FA050hYDnJ97KWdYw8%2BNhrSoJcgukHPKUB6%2FinRuNz9x1HMumci27PCSI8GEF59e3U7Ku2AFonGqoPHSF4CPNupJ7pv%2Fx9J%2F3QqqqwM5eet26dxeHIDLp4dVhAlkvlkfvoc6ZOP2LBPwsvtb%2BE0dcsMD6vQGF%2ByXsqpgJ0Nc%2BhxQU1ROwnYEPOMMFA94x%2FwTzVmEV3VqxSLsXtn14BwrBllWqPng8P%2FuqPeR%2BD%2Bt6AbmqBHL7B4oUxirh%2Bi6wAjvxZNTEmnPfFKm8EceLnFvo0kHB77kpygjbzPPSiiJc7gI4Hwe%2BK05RD9hCn1p1LDdPridZYIxxrZe1%2BW6gCP%2BBaMFejZDw1FoFIeXiiQhsOVcYc5cOpQrh8QWQWauN31rsEgs%2FNifY%2Fl1ULCUbdmPMiRC36PaXb9jV0sOMYGwSS7vaxCf5%2BY9rqY8xHmg2e88QSIxNuMwx6zfygY6pgGWLQBBKzCuo9Jd6a8lSn%2F59ja519xHy7aRAojdZHRUrIHcHiRd4N11dSyLorRS8u9kR01fRlOgSBztfe0bCjfNX%2FlM9bDvc%2FqCQBmed4UccOdeDovod%2BvG1xC9lo7qHFI%2F97AoarzZ6wM3nH7VMpQYEVqboEeaCc84D1aHARwEQ9vKuv4Cj07uiSGu3ehdX2r0HimQ32Sp6q9yJPt%2FqwjdW2AuxGrI&X-Amz-Signature=b336c358c1a8fb9519ccd5d11b091cb3d1ec0f04d8e8bc5d1a8e513e4cc51b0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







