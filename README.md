



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AE5BEOP%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T180711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIH1gj5kptuYNJ8E951bxrPMMRCK7HVArBVn%2BwsylGWjuAiEA%2Bz2c8GUknbfYKCw4p4MImqD3SXHSSROjuOpDkmTG4aIqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVZCeIvW1Y6xxxGPircA9YEDd5C%2FeKmxjgS0kwg%2BcCvkvQvqGcoky0Z9rIeZ8oVQgAK5K9m9UNqDNIB81nmMt6LZZljHyO872P4bqx75P7XQKjoVSTriF1Nw9SCAMI4c0OJnLFi2peGpUxhVpFBoUSnTp1xL%2Fks8Ed%2BpqgCUjd4r0xpqbkXtaY9XGeLWPq9L28JRYhXqoCsvguk51uHX4Li54yGenP2AValTl92%2BE97loqtSbf3grE8PDtOyTzlIjiCAy90BHSfvQFd0iTmbJ%2B%2FMnKt3F8WBc8dytj58b1QaK%2B9deObe%2BQXtTWUcdmf1KUuklVznvRxikMeFpKwcm1KlqmW3h0tGzDcuENqWyf2Z9ZW0iCFcIHw85joqLd7N0D8wWJbR9p0dH5ZmSF%2FIuEXS4sb0msqzo0CuINsuOJhaKcsjBgeYzis8siT1AEqMJ0Wm%2Bv1nZ%2Bdrkv6vH9yfwgaepMSHyqEHWsH4MC53CIbMwoyg4eC%2FKf%2FPy7DHHC1bMeN4dVa8xWidNqPgRgAHW8QB9HTywTCOyh%2FihIm9%2FQUIVdOVHjD8%2FAkL8hFXhqVAM%2BiHYfmqX%2FSEtt8CFelq4fkbCM%2BIyoJe9ZIZSsEXhWj5iw6RpX2U8jymkCNkFyL0w1IkdgaTivqwVT7MI70t9cGOqUBavnO9kOT3s%2Bjvbl0pXY5aJNptzsvq5l5LjzT%2FXY%2FMZD99m0Iwx9CzFl7DgKLwNFcV%2FfvafIY3zfIBRsFJDFivvB0ms5HSqT2nfHccFSmn0ht1j1J8%2Fl3fheY%2FzEb0IyrQ%2FdjbTDh7lMW9cxkdtr%2FVMAoU9dah3F8pdUk5O9Waoj73EnCopda%2F%2FHGzmcDRKfsIzz83mYlJ8MGSRAksje7puOZToKh&X-Amz-Signature=399880f3fed8879d4ab8561b35283f1c8d871a0b104a4155deee09e9a6a4e0e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AE5BEOP%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T180711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIH1gj5kptuYNJ8E951bxrPMMRCK7HVArBVn%2BwsylGWjuAiEA%2Bz2c8GUknbfYKCw4p4MImqD3SXHSSROjuOpDkmTG4aIqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOVZCeIvW1Y6xxxGPircA9YEDd5C%2FeKmxjgS0kwg%2BcCvkvQvqGcoky0Z9rIeZ8oVQgAK5K9m9UNqDNIB81nmMt6LZZljHyO872P4bqx75P7XQKjoVSTriF1Nw9SCAMI4c0OJnLFi2peGpUxhVpFBoUSnTp1xL%2Fks8Ed%2BpqgCUjd4r0xpqbkXtaY9XGeLWPq9L28JRYhXqoCsvguk51uHX4Li54yGenP2AValTl92%2BE97loqtSbf3grE8PDtOyTzlIjiCAy90BHSfvQFd0iTmbJ%2B%2FMnKt3F8WBc8dytj58b1QaK%2B9deObe%2BQXtTWUcdmf1KUuklVznvRxikMeFpKwcm1KlqmW3h0tGzDcuENqWyf2Z9ZW0iCFcIHw85joqLd7N0D8wWJbR9p0dH5ZmSF%2FIuEXS4sb0msqzo0CuINsuOJhaKcsjBgeYzis8siT1AEqMJ0Wm%2Bv1nZ%2Bdrkv6vH9yfwgaepMSHyqEHWsH4MC53CIbMwoyg4eC%2FKf%2FPy7DHHC1bMeN4dVa8xWidNqPgRgAHW8QB9HTywTCOyh%2FihIm9%2FQUIVdOVHjD8%2FAkL8hFXhqVAM%2BiHYfmqX%2FSEtt8CFelq4fkbCM%2BIyoJe9ZIZSsEXhWj5iw6RpX2U8jymkCNkFyL0w1IkdgaTivqwVT7MI70t9cGOqUBavnO9kOT3s%2Bjvbl0pXY5aJNptzsvq5l5LjzT%2FXY%2FMZD99m0Iwx9CzFl7DgKLwNFcV%2FfvafIY3zfIBRsFJDFivvB0ms5HSqT2nfHccFSmn0ht1j1J8%2Fl3fheY%2FzEb0IyrQ%2FdjbTDh7lMW9cxkdtr%2FVMAoU9dah3F8pdUk5O9Waoj73EnCopda%2F%2FHGzmcDRKfsIzz83mYlJ8MGSRAksje7puOZToKh&X-Amz-Signature=7efa53161b3df894b2b198e37b844aa1d8c5e2e46119301c616846b665724f9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







