Title: My understanding of PyTorch
Date: 2018-08-08 15:01
Modified: 2018-08-13 15:30
Category: Deep Learning
Tags: torch, deeplearning
Slug: understand-torch
Authors: Bhaskar C
Summary: My understanding of PyTorch.

Yo,  
This will be blog on my understanding on pytorch. I am following the [official tutorial](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html) for the same.  
First of all, let me tell you that I took two days to finish the 60 minute blitz. To be honest, I was distracted and had other work too. And [Soumith Chintala](http://soumith.ch/) has explained it in the best possible way. I loved the tutorial and now I feel like I can start off a new project with PyTorch without any fear.  
There are four parts to the tutorial, namely:
- What is PyTorch?
- Neural networks
- Training the classifier
- Data Parallelism (*Optional*)  
##  **What is PyTorch?**  
Here the author talks about Tensors and operations related to them. He then talks about Autograd function and gradients.  
Tensors are similar to *numpy arrays*, difference being that the tensors can be *loaded into GPU* for faster computing. One can create a tensor in many ways, like create one with uninitialized values, random values, zeros or directly feed data.  
You can operate on these tensors like a matrix, one can add, subtract, multiply, perform scalar multiplication/division on them. These operations help in creating the *graph* which is the core of PyTorch.  
The tensors can be converted into numpy arrays directly with a  simple command *add code here*. The converted numpy arrays occupy the same space as tensors, so any changes made to these numpy arrays will result in changes to the tensors. Basically it is like accessing the same values as *tesnors* or as *numpy arrays*, it is left to the user.  
Tensors can be moved to GPU using simple command *add code here*.  
**Autograd: Automatic differentiation**  
Central to all neural networks in PyTorch is `autograd` package. This package provides automatic differentiation for all operations on Tensors. It is a define-by-run framework, which means that your backprop is defined by how your code is run, and that every single iteration can be different.  
In tensors, one can set the `requires_grad` attribute as `True`, this starts to track all the operations on it. After the required **Graph** is created, i.e, the architecture and the connections/computations are completed, one can run `.backward()` and have all the gradients computed automatically. The gradient for this tensor will be accumulated into `.grad` attribute.  
For evaluating a model, one can turn off the tracking by wrapping one's code block in `with torch.no_grad():`.  
One can define one's own operations and define the forward pass and backward function. This will be an extension to the autograd operation. Refer this [link](https://pytorch.org/docs/stable/autograd.html#torch.autograd.Function).  


## **Neural Networks**
The most fascinating thing about PyTorch was the freedom it gave to write your own layers with ease and integrate to the network flow. Also, the dynamic graph is much better than the tensorflow's static graph, i.e, say you have added two tensors, then the output can be viewed without creating a session to run the graph, which is required in tensorflow.