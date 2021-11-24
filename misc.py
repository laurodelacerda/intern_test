# -*- coding: utf-8 -*-
"""
author: Lauro de Lacerda
e-mail: lauro.lacerda@metaltoad.com

Intern Exam
"""

import math


def add(number1 :float, number2 :float) -> float:
    return number1 + number2


def truncate(value :float, ndigits :int) -> float:
    """ Truncate a float to the desired number of decimals

        Args: 
            value (float) : The number to be truncated
            ndigits (int) : The number of digits to truncate the value

        Returns:
            var (float): The truncated value
    """

    stepper = 10.0 ** ndigits
    return math.trunc(stepper * value) / stepper


def check_eligible_state(state :str) -> float:
    ''' It checks if one state is eligible to some random policies.
    
        Args:
            state (string): The State in Brazil

        Returns:
            variable (bool): Whether the state is eligible
    '''
         
    policy_1 = state in ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS']        
    policy_2 = state in ['MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    policy_3 = state in ['ES', 'MG', 'RJ', 'SP']

    if (policy_1 or policy_2) and policy_3:
        return True
    else: 
        return False 


def calculate_hours(total_pay :float, pay_rate :float) -> float:
    """ Calculate the amount of hours an employee should work to deserve certain salary.

        Args:
            total_pay (float): The value for total pay 
            pay_rate (float): The value for pay rate

        Return:
            variable (float): The value for hour
    """
    
    try:
        return total_pay / pay_rate
    except ZeroDivisionError:
        return 0


def calculate_taxes(taxes :list, total_pay :float):
    """ Calculate the annual taxes for a certain occupation

        Args:
            taxes (list):      List of floats that represent taxes e.g.: [0.5, 0.2, 0.3]
            total_pay (float): Total pay for a certain occupation  e.g.: 15000

        Returns:
            values_tax (list): List of values to be taxed
    """

    if not taxes:
        return 0

    values_tax = list()
    for i in taxes:
        
        values_tax.append(i * total_pay)

    return values_tax


def save_grades(students: list, grades :list):
    """ Save Grades for a group of students.

        Args:
            students (list): List of Students e.g.: ['A', 'B', 'C']
            grades (list):   List of Grades   e.g.: [9.0, 8.5, 7.6]

        Returns:
            students_grades (dict): Map of students and grades
    """

    if len(students) != len(grades):
        return 'Lists lenghts should be the same for students and grades'

    students_grades = dict()

    for i, item in enumerate(students):
        students_grades[item] = grades[i]

    return students_grades
