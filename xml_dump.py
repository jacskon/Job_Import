from wsgiref import simple_server
import application
import pdb
job_properties = """jobName1    jobParams1    jobTarget1    jobTargetType1    jobCredentials1    jobDescription1
jobName2    jobParams2    jobTarget2    jobTargetType2    jobCredentials2    jobDescription2
"""

def xml_build(excel_string):
    newArray = []
    values = excel_string.splitlines()
    for x in values:
        newArray.append(x.split("    "))
    body = ""
    header = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <Jobsdata>
        <createdBy>SYSMAN</createdBy>
        <creationDate>2015-06-11T15:17:40.732+10:00</creationDate>
        <coreReleaseVersion>12.1.0.4.0</coreReleaseVersion>
        <productReleaseVersion>12.1.0.4.0</productReleaseVersion>
        <productVersion>12c</productVersion>
        <releaseNumber>4</releaseNumber>
        <jobList>"""
    job_array = newArray
    for x in job_array:
        body += """
                <jobData>
                    <job>
                        <credentialUsages>
                            <credentialReference>
                                <name>""" + x[4] + """</name>
                                <owner>OPS_ADMIN</owner>
                                <type>NAMED</type>
                            </credentialReference>
                            <description>Credentials to authenticate on the host to execute the command or script.</description>
                                <name>&lt;all_targets&gt;</name>
                                <type>host</type>
                            <usage>defaultHostCred</usage>
                        </credentialUsages>
                        <description>""" + str(x[5]) + """</description>
                        <correctiveAction>false</correctiveAction>
                        <libraryJob>true</libraryJob>
                        <name>""" + x[0] + """</name>
                        <owner>OPS_ADMIN</owner>
                        <schedule>
                            <frequency>IMMEDIATE</frequency>
                            <gracePeriod>-1</gracePeriod>
                            <interval>0</interval>
                            <timeZone>
                                <targetIndex>1</targetIndex>
                                <type>TIMEZONE_TARGET</type>
                            </timeZone>
                        </schedule>
                        <status>ACTIVE</status>
                        <targetType>host</targetType>
                        <targets>
                            <name>""" + x[1] + """</name>
                            <type>""" + x[3] + """</type>
                        </targets>
                        <type>OSCommand</type>
                        <variables>
                            <description>Comma separated list of parameters to the command.
        For example, if the command is &quot;ls&quot; the args might be &quot;-l,file1,file2&quot;.
        [Deprecated] Use no_shell_command instead.</description>
                            <name>args</name>
                            <required>false</required>
                            <secret>false</secret>
                            <type>Scalar</type>
                            <value>/bin/sh -x</value>
                        </variables>
                        <variables>
                            <description>The command to run on the target (without a shell).
        Useful when parsing the command line is not supported,
        especially when privilege delegation is enabled.
        [Deprecated] Use no_shell_command instead.</description>
                            <name>command</name>
                            <required>false</required>
                            <secret>false</secret>
                            <type>Scalar</type>
                            <value>%job_default_shell%</value>
                        </variables>
                        <variables>
                            <description>OS Script to run on the target.</description>
                            <name>large_os_script</name>
                            <required>false</required>
                            <secret>false</secret>
                            <type>Scalar</type>
                            <value> """ + x[1] + """
                            </value>
                        </variables>
                    </job>
                </jobData>"""
    footer = """
    </jobList>
    </Jobsdata>"""
    xml_output = header + body + footer
    text_file = open("Output.xml", "w")
    text_file.write(xml_output)
    text_file.close()
    return xml_output

if __name__ == '__main__':

    server = simple_server.make_server('localhost', 8080, application)
    print "Listening on http://localhost:8080/"
    server.serve_forever()