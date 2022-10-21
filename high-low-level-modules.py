# High level module is the interface / abstraction that will be consumed directly by the presentation layer.
# Low level on the other hand are bunch of small modules (subsystems) help the high level do their work.
# Example below is the high level module.

public class OrderService : IOrderService
{
    public void InsertOrder(Order ord)
    {
        if(orderValidator.IsValidOrder(ord)
        {
            orderRepository.InsertNew(ord);
            userNotification.Notify(ord);
        }
    }
}

# Low level module

public class OrderValidator : IOrderValidator
{
    public bool IsValidOrder(Order ord)
    {
        if(ord == null)
            throw new NullArgumentException("Order is null");
        else if(string.IsNullOrEmpty(ord.CustomerId))
            throw new InvalidArgumentException("Customer is not set");
        else if(ord.Details == null || !ord.Details.Any())
            throw new InvalidArgumentException("Order detail is empty");
    }
}

# High Level Module --> this module represent more business aspect rather than technical aspect.
# It can be refered as an abstraction rather than implementation, and usually achieved through interfaces.
#
# Some example maybe: RegisterAccount, PostAnswer, PostQuestion, AddComment, InsertComment.
#
# Since Low Level Module represent more technical aspect rather than the business aspect.
# Say for example we take the InsertComment HLM. The LLM should be:
#
# Open database connection
# Execute insert statement
# Close database connection
# A High Level Module can be a Low Level Module in another context. Taking another example, AddComment's LLM should be:
#
# Validate the comment (e.g. 15 char min) --> this will be another HLM
# Insert comment to database --> this will be another HLM (InsertComment)
# Add notification to involved user --> this will be another HLM
# The same apply for other HLM as well.