#prefix with the package folder name
#one way of importing whole package
"""
import ecommerce.shipping
ecommerce.shipping.calculateShipping()

"""

#Importing only specific method(s)
"""

from ecommerce.shipping import calculateShipping, anotherMethod
calculateShipping()
"""

#Import the specific module
"""
from ecommerce import shipping
shipping.calculateShipping()

"""