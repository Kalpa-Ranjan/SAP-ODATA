



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HEBC3O7%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T182221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCID9hB1aTfZcUSnXdUt%2FkG%2FAyOx836wF%2B3%2FfwE109hwDDAiAK4wHX011u3DJhTM%2FsGUglQPsK2ezfCgAPsm9MIN7ykCr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIM2PwUn3rmkXdosp72KtwDLV4hWz%2BKNIHVP%2BRSfbkOUjSEaGPOp0BCtd26FHiZwkoJFP9WxU5VI0Z%2FVujNq%2BFYBcpHSaBbO9r4TFZhSXI8Aj9tcJQfO%2BfbOrW5kbHFxrAQu9%2FqHTLNvEIcvs0hFX3JqiHEfxu%2BbJ9M%2FrQTY5982RjRvg2bJhlPwOG%2FADovzFCju79EN4lOzrfRDtQcn4TKeSmsdFZVXDs%2FgvEW5IYWlX8Tp1sLJiYgkEq5p7jPIKtjwUj%2BC0y30qh7OILLKuk4E2DJHIH4LUXBZVxhFBkxIgf%2Fmtytyx9308ZJ9hUYCuP1zLK2RyVTZdbwFYyK84imk%2Fa2mgjSPpPXWq%2Burn314CLMmu2y1EprpymLe%2FjFVAZ7SblJ0xM3G8LdCh0ov3Rz%2BVELeiCSWapmCGlmsnVhYhMj5uqDtd%2BSspBEJh1l8Ax0axjjgeQ7k%2BMuhhk8EduXzvMo5kyMiT78jkMpXIsxqTSB0tXYMaCQhltKl1yTp2h5zE2bR9btztwdji9Re%2BhipzVCDgQQw3YxjZh1RCM44HmChLZJdkcSSyaWWm6V9%2FkSw%2F4bQWUjjK0NvWZk1ZzA0kGcNfaePVVv5G0GpdXfd2WKOL7WlGwl%2FdcKMjWIVexZjmN43R9ia8CdPa4wspbkygY6pgGgBtBsKBta7VCmdW%2BL9rGVvInOsjU8%2FckC6f%2B%2BqN%2B2e%2FDwR5i19ncli93ypiXfh%2Fsbb8ySjfPQKEUeMWn4VjeK5oiss%2BtB1A5aQ8SjqTJpts06awPPKBW8x9w%2FLUdolOXdh7r48g%2FVJfADXrJrl1%2F9zof44QNhoP1aSLWunnZvkTAaqe5PN12ylKP3h%2Bk3d62GS87HekeIyuk7PgYgmnS7KMj0ylVt&X-Amz-Signature=0b7bb80861cd9971feab73dc0d434fc5d3876dec3e55e172b99807e2fe3f251a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HEBC3O7%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T182221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCID9hB1aTfZcUSnXdUt%2FkG%2FAyOx836wF%2B3%2FfwE109hwDDAiAK4wHX011u3DJhTM%2FsGUglQPsK2ezfCgAPsm9MIN7ykCr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIM2PwUn3rmkXdosp72KtwDLV4hWz%2BKNIHVP%2BRSfbkOUjSEaGPOp0BCtd26FHiZwkoJFP9WxU5VI0Z%2FVujNq%2BFYBcpHSaBbO9r4TFZhSXI8Aj9tcJQfO%2BfbOrW5kbHFxrAQu9%2FqHTLNvEIcvs0hFX3JqiHEfxu%2BbJ9M%2FrQTY5982RjRvg2bJhlPwOG%2FADovzFCju79EN4lOzrfRDtQcn4TKeSmsdFZVXDs%2FgvEW5IYWlX8Tp1sLJiYgkEq5p7jPIKtjwUj%2BC0y30qh7OILLKuk4E2DJHIH4LUXBZVxhFBkxIgf%2Fmtytyx9308ZJ9hUYCuP1zLK2RyVTZdbwFYyK84imk%2Fa2mgjSPpPXWq%2Burn314CLMmu2y1EprpymLe%2FjFVAZ7SblJ0xM3G8LdCh0ov3Rz%2BVELeiCSWapmCGlmsnVhYhMj5uqDtd%2BSspBEJh1l8Ax0axjjgeQ7k%2BMuhhk8EduXzvMo5kyMiT78jkMpXIsxqTSB0tXYMaCQhltKl1yTp2h5zE2bR9btztwdji9Re%2BhipzVCDgQQw3YxjZh1RCM44HmChLZJdkcSSyaWWm6V9%2FkSw%2F4bQWUjjK0NvWZk1ZzA0kGcNfaePVVv5G0GpdXfd2WKOL7WlGwl%2FdcKMjWIVexZjmN43R9ia8CdPa4wspbkygY6pgGgBtBsKBta7VCmdW%2BL9rGVvInOsjU8%2FckC6f%2B%2BqN%2B2e%2FDwR5i19ncli93ypiXfh%2Fsbb8ySjfPQKEUeMWn4VjeK5oiss%2BtB1A5aQ8SjqTJpts06awPPKBW8x9w%2FLUdolOXdh7r48g%2FVJfADXrJrl1%2F9zof44QNhoP1aSLWunnZvkTAaqe5PN12ylKP3h%2Bk3d62GS87HekeIyuk7PgYgmnS7KMj0ylVt&X-Amz-Signature=7c722e37e7707d9f0dd75ef04cfa683f6bae69a8c89bada7c421b1ce381d59a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







