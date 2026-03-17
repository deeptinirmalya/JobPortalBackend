
def login_alert(time, user_name):
    subject = "Security Alert: Unusual Login Detected"
    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Security Alert - Account Login Detected</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    
                    <!-- Header with Warning -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%); padding: 40px 30px; text-align: center;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <div style="width: 70px; height: 70px; background-color: rgba(255,255,255,0.2); border-radius: 50%; display: inline-block; text-align: center; line-height: 70px; margin-bottom: 20px;">
                                            <span style="font-size: 40px; color: #ffffff;">⚠️</span>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 28px; font-weight: 600;">Security Alert</h1>
                                        <p style="margin: 0; color: #ffffff; font-size: 16px; opacity: 0.95;">Unusual login activity detected</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Hello <strong>{user_name}</strong>,
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                We detected a login to your account that appears slightly unusual. This could be a routine login from a new location or device, but we wanted to make sure it was you.
                            </p>

                            <!-- Critical Alert Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #856404; font-size: 15px; font-weight: 600;">
                                            ⚠️ Action Required - Review This Login
                                        </p>
                                        <p style="margin: 0; color: #856404; font-size: 14px; line-height: 1.6;">
                                            This login attempt has been flagged due to unusual patterns. Please verify that this was you.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Time Display -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8f9fa; border-left: 4px solid #ff6b6b; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #495057; font-size: 14px; font-weight: 600;">Login Time:</p>
                                        <p style="margin: 0; color: #212529; font-size: 18px; font-weight: 600;">{time}</p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Security Warning -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8d7da; border-left: 4px solid #dc3545; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #721c24; font-size: 15px; font-weight: 600;">
                                            🔒 If This Wasn't You
                                        </p>
                                        <p style="margin: 0; color: #721c24; font-size: 14px; line-height: 1.6;">
                                            Please <strong>change your password immediately</strong> to secure your account. We recommend using a strong, unique password and enabling two-factor authentication for added security.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Security Tips -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #e7f3ff; border-left: 4px solid #0066cc; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #004085; font-size: 14px; font-weight: 600;">
                                            🛡️ Security Recommendations:
                                        </p>
                                        <ul style="margin: 0; padding-left: 20px; color: #004085; font-size: 14px; line-height: 1.8;">
                                            <li>Use a strong, unique password for your account</li>
                                            <li>Never share your password with anyone</li>
                                        </ul>
                                    </td>
                                </tr>
                            </table>

                            <p style="margin: 0; color: #666666; font-size: 14px; line-height: 1.6;">
                                If you have any questions or need assistance securing your account, our support team is available 24/7 to help you.
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e9ecef;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <p style="margin: 0 0 10px 0; color: #667eea; font-weight: 600; font-size: 18px;">HireNest Team Platform</p>
                                        <p style="margin: 0 0 15px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            © 2026 HireNest Team. All rights reserved.<br>
                                            Your security is our top priority.
                                        </p>
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                            <tr>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Privacy Policy</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Terms of Service</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Support</a>
                                                </td>
                                            </tr>
                                        </table>
                                        <p style="margin: 15px 0 0 0; color: #adb5bd; font-size: 12px;">
                                            123 Business Street, Suite 100, City, State 12345<br>
                                            This is an automated security alert. Please do not reply to this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                </table>

                <!-- Mobile-only text -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 20px auto 0;">
                    <tr>
                        <td align="center" style="color: #999999; font-size: 12px; padding: 0 20px;">
                            You received this security alert because unusual activity was detected on your HireNest Team account.
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""
    templets = {
        "subject": subject,
        "body": body
    }
    return templets


def verify_email_templetes(url, email):
    subject = "Account Verification Alert"

    body = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Verify Your Email Address</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <div style="width: 80px; height: 80px; background-color: rgba(255,255,255,0.2); border-radius: 50%; display: inline-block; text-align: center; line-height: 80px; margin-bottom: 20px;">
                                            <span style="font-size: 45px; color: #ffffff;">✉️</span>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 28px; font-weight: 600;">Verify Your Email</h1>
                                        <p style="margin: 0; color: #ffffff; font-size: 16px; opacity: 0.95;">Complete your account setup</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="margin: 0 0 20px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Hello,
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Thank you for signing up with <strong>HireNest Team Platform</strong>! We're excited to have you on board.
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                To complete your registration and start using your account, please verify your email address by clicking the button below:
                            </p>

                            <!-- Email Display Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8f9fa; border-left: 4px solid #667eea; border-radius: 6px; margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 8px 0; color: #6c757d; font-size: 13px; font-weight: 500;">Your Email Address:</p>
                                        <p style="margin: 0; color: #212529; font-size: 16px; font-weight: 600;">{email}</p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Verify Button -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 30px;">
                                <tr>
                                    <td align="center" style="padding: 10px 0;">
                                        <a href="{url}" style="display: inline-block; padding: 16px 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #ffffff; text-decoration: none; font-weight: 600; font-size: 16px; border-radius: 8px; box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);">Verify Email Address</a>
                                    </td>
                                </tr>
                            </table>

                            <!-- Alternative Link -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f8f9fa; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #495057; font-size: 14px; font-weight: 600;">
                                            Button not working?
                                        </p>
                                        <p style="margin: 0 0 10px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            Copy and paste this link into your browser:
                                        </p>
                                        <p style="margin: 0; word-break: break-all;">
                                            <a href="{url}" style="color: #667eea; font-size: 13px; text-decoration: none;">{url}</a>
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- Info Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #fff3cd; border-left: 4px solid #ffc107; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 15px 20px;">
                                        <p style="margin: 0; color: #856404; font-size: 13px; line-height: 1.6;">
                                            <strong>⏱️ Important:</strong> This verification link will expire in 24 hours for security purposes. If you didn't create an account with us, please ignore this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <p style="margin: 0; color: #666666; font-size: 14px; line-height: 1.6;">
                                Once verified, you'll have full access to all features of HireNest Team Platform. If you have any questions, feel free to reach out to our support team.
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e9ecef;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <p style="margin: 0 0 10px 0; color: #667eea; font-weight: 600; font-size: 18px;">HireNest Team Platform</p>
                                        <p style="margin: 0 0 15px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            © 2026 HireNest Team. All rights reserved.<br>
                                            Building better experiences together.
                                        </p>
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                            <tr>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Privacy Policy</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Terms of Service</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Support</a>
                                                </td>
                                            </tr>
                                        </table>
                                        <p style="margin: 15px 0 0 0; color: #adb5bd; font-size: 12px;">
                                            123 Business Street, Suite 100, City, State 12345<br>
                                            This is an automated message. Please do not reply to this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                </table>

                <!-- Mobile-only text -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 20px auto 0;">
                    <tr>
                        <td align="center" style="color: #999999; font-size: 12px; padding: 0 20px;">
                            You received this email because you created an account with HireNest Team Platform.
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""
    
    result = {
        "subject": subject,
        "body": body
    }
    return result


def company_details_uploaded():
    subject = "Thank You - Details Uploaded Successfully"

    
    body = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Company Details Uploaded Successfully</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f4f4f4;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 40px 30px; text-align: center;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <div style="width: 80px; height: 80px; background-color: rgba(255,255,255,0.2); border-radius: 50%; display: inline-block; text-align: center; line-height: 80px; margin-bottom: 20px;">
                                            <span style="font-size: 45px; color: #ffffff;">✓</span>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center">
                                        <h1 style="margin: 0 0 10px 0; color: #ffffff; font-size: 28px; font-weight: 600;">Details Uploaded Successfully!</h1>
                                        <p style="margin: 0; color: #ffffff; font-size: 16px; opacity: 0.95;">Thank you for joining us</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px 30px;">
                            <p style="margin: 0 0 20px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Dear Partner,
                            </p>
                            <p style="margin: 0 0 25px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                <strong>Thank you for joining HireNest Platform!</strong> We're excited to have you as part of our growing community.
                            </p>
                            <p style="margin: 0 0 30px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                Your company details have been uploaded successfully and are now under review by our team.
                            </p>

                            <!-- Success Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #d4edda; border-left: 4px solid #28a745; border-radius: 6px; margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #155724; font-size: 15px; font-weight: 600;">
                                            ✅ Submission Complete
                                        </p>
                                        <p style="margin: 0; color: #155724; font-size: 14px; line-height: 1.6;">
                                            Your company information has been received and is being processed by our verification team.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <!-- What's Next Section -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 25px;">
                                <tr>
                                    <td>
                                        <h2 style="margin: 0 0 20px 0; color: #333333; font-size: 20px; font-weight: 600;">What Happens Next?</h2>
                                    </td>
                                </tr>
                            </table>

                            <!-- Steps -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 30px;">
                                <tr>
                                    <td style="padding: 15px 0; border-bottom: 1px solid #e9ecef;">
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="40" valign="top">
                                                    <div style="width: 30px; height: 30px; background-color: #667eea; border-radius: 50%; color: #ffffff; text-align: center; line-height: 30px; font-weight: 600; font-size: 14px;">1</div>
                                                </td>
                                                <td valign="top">
                                                    <p style="margin: 0 0 5px 0; color: #333333; font-size: 15px; font-weight: 600;">Review Process</p>
                                                    <p style="margin: 0; color: #6c757d; font-size: 14px; line-height: 1.5;">Our team will carefully review your submitted information and documents.</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 15px 0; border-bottom: 1px solid #e9ecef;">
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="40" valign="top">
                                                    <div style="width: 30px; height: 30px; background-color: #667eea; border-radius: 50%; color: #ffffff; text-align: center; line-height: 30px; font-weight: 600; font-size: 14px;">2</div>
                                                </td>
                                                <td valign="top">
                                                    <p style="margin: 0 0 5px 0; color: #333333; font-size: 15px; font-weight: 600;">Verification</p>
                                                    <p style="margin: 0; color: #6c757d; font-size: 14px; line-height: 1.5;">We'll verify all details to ensure compliance and accuracy.</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 15px 0;">
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="40" valign="top">
                                                    <div style="width: 30px; height: 30px; background-color: #667eea; border-radius: 50%; color: #ffffff; text-align: center; line-height: 30px; font-weight: 600; font-size: 14px;">3</div>
                                                </td>
                                                <td valign="top">
                                                    <p style="margin: 0 0 5px 0; color: #333333; font-size: 15px; font-weight: 600;">Notification</p>
                                                    <p style="margin: 0; color: #6c757d; font-size: 14px; line-height: 1.5;">Our team will inform you via email once the verification is complete.</p>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>

                            <!-- Info Box -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #e7f3ff; border-left: 4px solid #0066cc; border-radius: 6px; margin-bottom: 25px;">
                                <tr>
                                    <td style="padding: 20px;">
                                        <p style="margin: 0 0 10px 0; color: #004085; font-size: 14px; font-weight: 600;">
                                            ⏱️ Expected Timeline
                                        </p>
                                        <p style="margin: 0; color: #004085; font-size: 14px; line-height: 1.6;">
                                            Our verification process typically takes 2-3 business days. You'll receive an email notification as soon as your account is approved and ready to use.
                                        </p>
                                    </td>
                                </tr>
                            </table>

                            <p style="margin: 0 0 20px 0; color: #333333; font-size: 16px; line-height: 1.6;">
                                In the meantime, feel free to explore our platform or reach out to our support team if you have any questions.
                            </p>

                            <p style="margin: 0; color: #666666; font-size: 14px; line-height: 1.6;">
                                We appreciate your patience and look forward to working with you!
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #f8f9fa; padding: 30px; text-align: center; border-top: 1px solid #e9ecef;">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td align="center">
                                        <p style="margin: 0 0 10px 0; color: #667eea; font-weight: 600; font-size: 18px;">HireNest Platform</p>
                                        <p style="margin: 0 0 15px 0; color: #6c757d; font-size: 13px; line-height: 1.5;">
                                            © 2026 HireNest. All rights reserved.<br>
                                            Building better partnerships together.
                                        </p>
                                        <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                            <tr>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Privacy Policy</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Terms of Service</a>
                                                </td>
                                                <td style="color: #dee2e6;">|</td>
                                                <td style="padding: 0 10px;">
                                                    <a href="#" style="color: #667eea; text-decoration: none; font-size: 13px;">Support</a>
                                                </td>
                                            </tr>
                                        </table>
                                        <p style="margin: 15px 0 0 0; color: #adb5bd; font-size: 12px;">
                                            123 Business Street, Suite 100, City, State 12345<br>
                                            This is an automated message. Please do not reply to this email.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>

                </table>

                <!-- Mobile-only text -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="max-width: 600px; margin: 20px auto 0;">
                    <tr>
                        <td align="center" style="color: #999999; font-size: 12px; padding: 0 20px;">
                            You received this email because you submitted company details to HireNest Platform.
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""

    result = {
    "subject": subject,
    "body": body
    }
    
    return result


# Example usage:
# email_body = company_details_uploaded()
# send_email(to=company_email, subject="Thank You - Details Uploaded Successfully", body=email_body)