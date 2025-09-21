"""
Static Analysis

This module provides basic static code analysis functionality
for analyzing code quality, complexity, and potential issues.

Author: Hackathon Participant
Date: September 2024
"""

import ast
import re
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class CodeIssue:
    """Represents a code issue found during analysis"""
    line_number: int
    issue_type: str
    message: str
    severity: str  # 'low', 'medium', 'high'

class StaticAnalyzer:
    """Static code analyzer for Python code"""
    
    def __init__(self):
        self.issues: List[CodeIssue] = []
    
    def analyze_code(self, code: str, filename: str = "unknown") -> Dict[str, Any]:
        """
        Perform static analysis on Python code
        
        Args:
            code: The Python code to analyze
            filename: Name of the file being analyzed
            
        Returns:
            Analysis results dictionary
        """
        self.issues = []
        
        try:
            # Parse the code into an AST
            tree = ast.parse(code, filename=filename)
            
            # Perform various analyses
            self._check_complexity(tree)
            self._check_naming_conventions(tree)
            self._check_imports(tree)
            self._check_functions(tree)
            
            # Calculate metrics
            metrics = self._calculate_metrics(code, tree)
            
            return {
                "filename": filename,
                "issues": [
                    {
                        "line": issue.line_number,
                        "type": issue.issue_type,
                        "message": issue.message,
                        "severity": issue.severity
                    }
                    for issue in self.issues
                ],
                "metrics": metrics,
                "total_issues": len(self.issues),
                "high_severity_issues": len([i for i in self.issues if i.severity == "high"])
            }
            
        except SyntaxError as e:
            return {
                "filename": filename,
                "error": f"Syntax error: {e}",
                "issues": [],
                "metrics": {},
                "total_issues": 0
            }
    
    def _check_complexity(self, tree: ast.AST) -> None:
        """Check for code complexity issues"""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check function length
                if len(node.body) > 50:
                    self.issues.append(CodeIssue(
                        line_number=node.lineno,
                        issue_type="complexity",
                        message="Function is too long (>50 lines)",
                        severity="medium"
                    ))
                
                # Check for nested loops
                nested_depth = self._get_nested_depth(node)
                if nested_depth > 3:
                    self.issues.append(CodeIssue(
                        line_number=node.lineno,
                        issue_type="complexity",
                        message=f"Function has too many nested levels ({nested_depth})",
                        severity="high"
                    ))
    
    def _check_naming_conventions(self, tree: ast.AST) -> None:
        """Check Python naming conventions"""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                    self.issues.append(CodeIssue(
                        line_number=node.lineno,
                        issue_type="naming",
                        message="Function name should be lowercase with underscores",
                        severity="low"
                    ))
            
            elif isinstance(node, ast.ClassDef):
                if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                    self.issues.append(CodeIssue(
                        line_number=node.lineno,
                        issue_type="naming",
                        message="Class name should be PascalCase",
                        severity="low"
                    ))
    
    def _check_imports(self, tree: ast.AST) -> None:
        """Check import statements"""
        imports = [node for node in ast.walk(tree) if isinstance(node, ast.Import)]
        import_froms = [node for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
        
        if len(imports) + len(import_froms) > 20:
            self.issues.append(CodeIssue(
                line_number=1,
                issue_type="imports",
                message="Too many imports (>20)",
                severity="medium"
            ))
    
    def _check_functions(self, tree: ast.AST) -> None:
        """Check function-related issues"""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Check for missing docstrings
                if not ast.get_docstring(node):
                    self.issues.append(CodeIssue(
                        line_number=node.lineno,
                        issue_type="documentation",
                        message="Function missing docstring",
                        severity="low"
                    ))
    
    def _get_nested_depth(self, node: ast.FunctionDef) -> int:
        """Calculate nesting depth of a function"""
        max_depth = 0
        current_depth = 0
        
        for child in ast.walk(node):
            if isinstance(child, (ast.For, ast.While, ast.If, ast.With, ast.Try)):
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif isinstance(child, (ast.For, ast.While, ast.If, ast.With, ast.Try)):
                current_depth -= 1
        
        return max_depth
    
    def _calculate_metrics(self, code: str, tree: ast.AST) -> Dict[str, Any]:
        """Calculate code metrics"""
        lines = code.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        
        return {
            "total_lines": len(lines),
            "non_empty_lines": len(non_empty_lines),
            "function_count": len(functions),
            "class_count": len(classes),
            "average_function_length": len(non_empty_lines) / max(len(functions), 1)
        }
