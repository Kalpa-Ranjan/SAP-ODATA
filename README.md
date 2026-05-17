



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2RQCA4K%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T023856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsX23e7BPrYompiSChrlwz5Tl3lU5lsS5Jmbeqq8VvCAiEAoifvxGb9hVCYRA%2FCwFMEBZGaJv8rs5rUOtPVzwZGQNsqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnxiEz1mxfRNu%2BsoircA5wj7Gk37Reo0vtDp9IeBFObww5Oll3Ui84qg02VuJH%2FtM4b9LTFMA8B3zC2mhTidkBb9MgiRAQkSI7%2FFtqRgH%2BEnFvmHBtrA1ik%2B8AWm%2B4tSwhKndoa4bVYy8Y5t8FxY4av23WqOeq9TzuYLYVs6jITQ43NMkQD%2FkXxO%2FnuM123l5whkcJ8ggOaFZKev%2F6EgJ%2FZWyq40YQ3Wy4gjAh7lqdxbjY8zMLbA0t1Z8vDUB%2BCQxJeeOnPWRd%2BYeG415R43Y61KAvczOkQps5aAEooe0CBq%2FsfBi7%2BtMvwu8EkCrx3sR%2FyRy4siaJDSXykJ8TgozLkGux5O4dz2Wdaqclc23xK0RRO4Kgr0QXEIT6AWYBoX5llb%2FjoleewrL4DKXUEnGY%2BoGf3jktblQN5sVzx31XGZDoPScXHjAu4Cjgw%2BnlVaaXP9GVZItqYxlCcOATOxiLrj5vg%2FyMQBJzpDdGenvlIJlBAu4wcQD3sf30HqJrC%2FUQBu9znGnyriDq140dCVAokHOic59fxFErFGbegtwKY3mdJ%2FH9j%2Bq0XysW6tGB9nxobz3cClPtsdMwftGjP1ER0ncQ71P5Wcxg7cea7aqZUG658reyuKHosSu9HhdtAO1ITcQ7wQ2BCtNgJMITOpNAGOqUB2aMTK3aFhVo4e26lcEWvcXpVPiyEog0qOGL%2Bxi3XHOu6zRFbBXIuJVz0Z%2FJ3%2B%2F3xY5ts1%2BQNfUaoVYMXAVkMlpxSIlKOS9rPXLuuMPVc0wFjQxQDnCeUmD56FP0mbehnP%2Ffv5SZLn9Iqg1ZSClwhKNa2j%2B2IxUDERda5PkFFrL3qP04Qg0otIH0fh%2FENAICdOCBhJbUSGtx6YX6u3ZSoMe5xFDpT&X-Amz-Signature=7b0c19c2c705ac24119abb399157c9107228c98415afeae3905618c52cd450b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2RQCA4K%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T023856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDsX23e7BPrYompiSChrlwz5Tl3lU5lsS5Jmbeqq8VvCAiEAoifvxGb9hVCYRA%2FCwFMEBZGaJv8rs5rUOtPVzwZGQNsqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGnxiEz1mxfRNu%2BsoircA5wj7Gk37Reo0vtDp9IeBFObww5Oll3Ui84qg02VuJH%2FtM4b9LTFMA8B3zC2mhTidkBb9MgiRAQkSI7%2FFtqRgH%2BEnFvmHBtrA1ik%2B8AWm%2B4tSwhKndoa4bVYy8Y5t8FxY4av23WqOeq9TzuYLYVs6jITQ43NMkQD%2FkXxO%2FnuM123l5whkcJ8ggOaFZKev%2F6EgJ%2FZWyq40YQ3Wy4gjAh7lqdxbjY8zMLbA0t1Z8vDUB%2BCQxJeeOnPWRd%2BYeG415R43Y61KAvczOkQps5aAEooe0CBq%2FsfBi7%2BtMvwu8EkCrx3sR%2FyRy4siaJDSXykJ8TgozLkGux5O4dz2Wdaqclc23xK0RRO4Kgr0QXEIT6AWYBoX5llb%2FjoleewrL4DKXUEnGY%2BoGf3jktblQN5sVzx31XGZDoPScXHjAu4Cjgw%2BnlVaaXP9GVZItqYxlCcOATOxiLrj5vg%2FyMQBJzpDdGenvlIJlBAu4wcQD3sf30HqJrC%2FUQBu9znGnyriDq140dCVAokHOic59fxFErFGbegtwKY3mdJ%2FH9j%2Bq0XysW6tGB9nxobz3cClPtsdMwftGjP1ER0ncQ71P5Wcxg7cea7aqZUG658reyuKHosSu9HhdtAO1ITcQ7wQ2BCtNgJMITOpNAGOqUB2aMTK3aFhVo4e26lcEWvcXpVPiyEog0qOGL%2Bxi3XHOu6zRFbBXIuJVz0Z%2FJ3%2B%2F3xY5ts1%2BQNfUaoVYMXAVkMlpxSIlKOS9rPXLuuMPVc0wFjQxQDnCeUmD56FP0mbehnP%2Ffv5SZLn9Iqg1ZSClwhKNa2j%2B2IxUDERda5PkFFrL3qP04Qg0otIH0fh%2FENAICdOCBhJbUSGtx6YX6u3ZSoMe5xFDpT&X-Amz-Signature=5356c335e01a14136aa62f74a7e3fdc799fd177781801d5334366bb0b4e71f0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







